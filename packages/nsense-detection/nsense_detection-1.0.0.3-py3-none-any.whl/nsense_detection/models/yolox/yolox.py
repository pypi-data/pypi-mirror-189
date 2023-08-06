import time
#import logging as logger
import torch
import cv2
import numpy as np

from .yolox_utils import multiclass_nms, postprocess, predictions_to_object
from .yolox_utils import preproc as preprocess

# import original modules
from ...utils.detector_utils import load_image, plot_results, reverse_letterbox, write_predictions, output_format  
from ...utils.image_utils import imread  
from ...utils.util import get_savepath

# ======================
# Parameters
# ======================
MODEL_PARAMS = {'yolox_nano': {'input_shape': [416, 416]},
                'yolox_tiny': {'input_shape': [416, 416]},
                'yolox_s': {'input_shape': [640, 640]},
                'yolox_m': {'input_shape': [640, 640]},
                'yolox_l': {'input_shape': [640, 640]},
                'yolox_darknet': {'input_shape': [640, 640]},
                'yolox_x': {'input_shape': [640, 640]}}

COCO_CATEGORY = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train",
    "truck", "boat", "traffic light", "fire hydrant", "stop sign",
    "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
    "sports ball", "kite", "baseball bat", "baseball glove", "skateboard",
    "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork",
    "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange",
    "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "couch", "potted plant", "bed", "dining table", "toilet", "tv",
    "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave",
    "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
    "scissors", "teddy bear", "hair drier", "toothbrush"
]

SCORE_THR = 0.4
NMS_THR = 0.45
MODEL_NAME = 'yolox_m'
HEIGHT = MODEL_PARAMS[MODEL_NAME]['input_shape'][0]
WIDTH = MODEL_PARAMS[MODEL_NAME]['input_shape'][1]

def inference(raw_img, net, model_type):
    img, ratio = preprocess(raw_img, (HEIGHT, WIDTH))
    #print(f'input image shape: {raw_img.shape}')
    img = img.transpose(2, 0, 1)
    img = np.expand_dims(img, axis=0)
    #out = net.run(['output'],{'images': img})
    #img = img.astype(np.float32)
    
    # to cuda
    if model_type=='v8.trt':
        #print("yolox.py trt inference")
        img = img.astype(np.float32)
        img = torch.from_numpy(img)
        img = img.cuda()
        out = net(img)
        out = out[None, :]
        out = np.array(out.cpu())
    else:
        out = net.run(img)

    return out, ratio


def predict(image_path, net, model_type, check_eval, benchmark=False, write_prediction=False, save_path='./results/result_x_test.png'):
    iou = 0.45
    thd = 0.25
    if check_eval is True:
        thd = 0.01
    
    raw_img = imread(image_path, cv2.IMREAD_COLOR)
    # inference
    #print('Start inference...')
    if benchmark:
        print('BENCHMARK mode')
        total_time = 0
        for i in range(50):
            start = int(round(time.time() * 1000))
            output, ratio = inference(raw_img, net, model_type)
            end = int(round(time.time() * 1000))
            if i != 0:
                total_time = total_time + (end - start)
            #print(f'\tprocessing time {end - start} ms')
        print(f'\taverage time {total_time / 49} ms')
    else:
        output, ratio = inference(raw_img, net, model_type)

    
    predictions = postprocess(output[0], (HEIGHT, WIDTH))[0]
    detect_object = predictions_to_object(predictions, raw_img, ratio, iou, thd)
    detect_object = reverse_letterbox(detect_object, raw_img, (raw_img.shape[0], raw_img.shape[1]))
    
    #write prediction
    if write_prediction:
        # plot result
        res_img = plot_results(detect_object, raw_img, COCO_CATEGORY)
        # save image
        savepath = get_savepath(save_path, image_path)
        print(f'saved at : {savepath}')
        cv2.imwrite(savepath, res_img)
        # save result
        pred_file = '%s.txt' % savepath.rsplit('.', 1)[0]
        write_predictions(pred_file, detect_object, raw_img, COCO_CATEGORY)
        print('write prediction.')

    #if args.profile:
    #    print(net.get_summary())
    json_out  = output_format(detect_object, raw_img, category=COCO_CATEGORY)
    #print('Script finished successfully.')
    return json_out
