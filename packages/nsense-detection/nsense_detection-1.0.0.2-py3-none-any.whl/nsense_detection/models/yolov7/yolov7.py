import time
import cv2
import numpy as np
import torch
# import original modules
#sys.path.append('../../utils')
#import logging as logger

from .yolov7_utils import *
from ...utils.detector_utils import load_image, plot_results, reverse_letterbox, write_predictions, output_format
from ...utils.image_utils import imread  # noqa: E402
from ...utils.util import get_savepath

#logger.basicConfig(level='DEBUG')

# os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# ======================
# Parameters
# ======================
MODEL_PARAMS = {'yolov7': {'input_shape': [640, 640], 'max_stride': 32, 'anchors':[
                    [12,16, 19,36, 40,28], [36,75, 76,55, 72,146], [142,110, 192,243, 459,401]
                    ]},
                'yolov7x': {'input_shape': [640, 640], 'max_stride': 32, 'anchors':[
                    [12,16, 19,36, 40,28], [36,75, 76,55, 72,146], [142,110, 192,243, 459,401]
                    ]},
                'yolov7_int8': {'input_shape': [640, 640], 'max_stride': 32, 'anchors':[
                    [12,16, 19,36, 40,28], [36,75, 76,55, 72,146], [142,110, 192,243, 459,401]
                    ]},
                'yolov7x_int8': {'input_shape': [640, 640], 'max_stride': 32, 'anchors':[
                    [12,16, 19,36, 40,28], [36,75, 76,55, 72,146], [142,110, 192,243, 459,401]
                    ]},
                'yolov7_w6': {'input_shape': [1280, 1280], 'max_stride': 64, 'anchors':[
                    [19,27, 44,40, 38,94 ], [96,68, 86,152, 180,137 ], [140,301, 303,264, 238,542], [436,615, 739,380, 925,792]
                    ]},
                'yolov7_e6': {'input_shape': [1280, 1280], 'max_stride': 64, 'anchors':[
                    [19,27, 44,40, 38,94 ], [96,68, 86,152, 180,137 ], [140,301, 303,264, 238,542], [436,615, 739,380, 925,792]
                    ]},
                'yolov7_d6': {'input_shape': [1280, 1280], 'max_stride': 64, 'anchors':[
                    [19,27, 44,40, 38,94 ], [96,68, 86,152, 180,137 ], [140,301, 303,264, 238,542], [436,615, 739,380, 925,792]
                    ]},
                'yolov7_e6e': {'input_shape': [1280, 1280], 'max_stride': 64, 'anchors':[
                    [19,27, 44,40, 38,94 ], [96,68, 86,152, 180,137 ], [140,301, 303,264, 238,542], [436,615, 739,380, 925,792]
                    ]},
                'yolov7_tiny': {'input_shape': [512, 512], 'max_stride': 32, 'anchors':[
                    [12,16, 19,36, 40,28], [36,75, 76,55, 72,146], [142,110, 192,243, 459,401]
                    ]}
                }

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

SCORE_THR = 0.25#0.4
NMS_THR = 0.45


#MODEL_NAME = 'yolov7'
#HEIGHT = MODEL_PARAMS[MODEL_NAME]['input_shape'][0]
#WIDTH = MODEL_PARAMS[MODEL_NAME]['input_shape'][1]
#STRIDE = MODEL_PARAMS[MODEL_NAME]['max_stride']
#ANCHORS = MODEL_PARAMS[MODEL_NAME]['anchors']

# ======================
# Main functions
# ======================
def inference(raw_img, net, model_type):
    
    HEIGHT = MODEL_PARAMS[net.name()]['input_shape'][0]
    WIDTH = MODEL_PARAMS[net.name()]['input_shape'][1]
    STRIDE = MODEL_PARAMS[net.name()]['max_stride']
    
    # Padded resize
    img = letterbox(raw_img, (HEIGHT, WIDTH), stride=STRIDE)[0]
    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB
    img = np.ascontiguousarray(img).astype(np.float32)
    img = img/255.0  # 0 - 255 to 0.0 - 1.0
    img_input = img[None, :, :, :]
       
    if model_type=='v8.trt':
        img_input = torch.from_numpy(img_input)
        img_input = img_input.cuda()
        out = net(img_input)
        out = [np.array(x.cpu()) for x in out]
        
        #out = np.array(out.cpu())
    else:
        out = net.run(img_input)
    #out = net.run(['output'],{'images': img[None, :, :, :]})
    #out = net.run(img[None, :, :, :])

    return out, img


def predict(image_path, net, model_type, check_eval, benchmark=False, write_prediction=False, save_path='./results/result_v7_test.png'):
    iou = 0.45
    thd = 0.25
    if check_eval is True:
        thd = 0.01
    STRIDE = MODEL_PARAMS[net.name()]['max_stride']
    ANCHORS = MODEL_PARAMS[net.name()]['anchors']

    raw_img = cv2.imread(image_path)  # BGR
    # inference
    #print('Start inference...')
    if benchmark:
        print('BENCHMARK mode')
        total_time = 0
        for i in range(50):
            start = int(round(time.time() * 1000))
            output, img = inference(raw_img, net, model_type)
            end = int(round(time.time() * 1000))
            if i != 0:
                total_time = total_time + (end - start)
            #print(f'\tprocessing time {end - start} ms')
        print(f'\taverage time {total_time / 49} ms')
    else:
        output, img = inference(raw_img, net, model_type)

    predictions = postprocess(output, ANCHORS, p6=STRIDE==64)[0]
    detect_object = predictions_to_object(predictions, raw_img, iou, thd, img.shape)
    

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
