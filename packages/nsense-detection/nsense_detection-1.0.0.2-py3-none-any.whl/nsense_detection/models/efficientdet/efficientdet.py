import time
#import logging as logger  
#import argparse
import numpy as np
import cv2
import torch
# import original modules
#sys.path.append('../../utils')
from .efficientdet_utils import *
from ...utils.detector_utils import load_image, plot_results, write_predictions, output_format  
from ...utils.util import get_savepath

#logger = getLogger(__name__)
#logger.basicConfig(level='DEBUG')

# ======================
# Parameters
# ======================

obj_list = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
    'fire hydrant', '', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep',
    'cow', 'elephant', 'bear', 'zebra', 'giraffe', '', 'backpack', 'umbrella', '', '', 'handbag', 'tie',
    'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
    'skateboard', 'surfboard', 'tennis racket', 'bottle', '', 'wine glass', 'cup', 'fork', 'knife', 'spoon',
    'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut',
    'cake', 'chair', 'couch', 'potted plant', 'bed', '', 'dining table', '', '', 'toilet', '', 'tv',
    'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink',
    'refrigerator', '', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier',
    'toothbrush']

NMS_THR = 0.2

def inference(img, net, iou, thd, model_type):
    dic_input_size = {
        'efficientdet_d0': 512,
        'efficientdet_d1': 640,
        'efficientdet_d2': 768,
        'efficientdet_d0_int8': 512,
        'efficientdet_d1_int8': 640,
        'efficientdet_d2_int8': 768
    }
    input_size = dic_input_size[net.name()]

    img, framed_metas = preprocess(img, input_size=input_size)
    #print(img.shape)
    #if not args.onnx:
    #    net.set_input_shape(img.shape)
    #    output = net.predict({'imgs': img})
    #else:
    #output = net.run(
    #    ['regression', 'classification', 'anchors'],
    #    {'imgs': img})
    
    if model_type=='v8.trt':
        img = img.astype(np.float32)
        img = torch.from_numpy(img)
        img = img.cuda()
        output = net(img)  
        output =[np.array(x.cpu()) for x in output]
        #output = np.array(out)
    else:
        output = net.run(img)
        
    regression, classification, anchors = output
    
    #regression= np.array(regression, dtype=np.float128)
    #classification= np.array(classification, dtype=np.float32) 
    #anchors= np.array(anchors, dtype=np.float32)
    
    
    threshold = thd
    iou_threshold = iou#args.iou_threshold
    out = postprocess(
        img,
        anchors, regression, classification,
        threshold, iou_threshold)

    out = invert_affine(framed_metas, out)

    return out


def predict(image_path, net, model_type, check_eval, benchmark, write_prediction=False, save_path='./results/result_effi_test.png'):
    iou = 0.2
    thd = 0.2
    if check_eval is True:
        thd = 0.2
        #print("evalmode")

    # prepare input data
    img = cv2.imread(image_path)
    #img = load_image(image_path)
    #print(f'input image shape: {img.shape}')
    #img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    
    #print('Start inference...')
    if benchmark:
       # if not args.profile:
       #     net.set_profile_mode(True)
        print('BENCHMARK mode')
        total_time = 0
        for i in range(50):
            start = int(round(time.time() * 1000))
            pred = inference(img, net, iou, thd, model_type)
            end = int(round(time.time() * 1000))
            if i != 0:
                total_time = total_time + (end - start)
            #print(f'\tprocessing time {end - start} ms')
        print(f'\taverage time {total_time / 49} ms')
    else:
        pred = inference(img, net, iou, thd, model_type)

    detect_object = predictions_to_object(pred, img.shape[1], img.shape[0])
    #write prediction
    if write_prediction:
        # plot result
        res_img = plot_results(detect_object, img, obj_list, logging=False)
        # save image
        savepath = get_savepath(save_path, image_path)
        print(f'saved at : {savepath}')
        cv2.imwrite(savepath, res_img)
        # save result
        pred_file = '%s.txt' % savepath.rsplit('.', 1)[0]
        write_predictions(pred_file, detect_object, img, obj_list)
        print('write prediction.')

    #if args.profile:
    #    print(net.get_summary())
    json_out  = output_format(detect_object, img)
    #print('Script finished successfully.')
    return json_out

