import cv2
import numpy as np
from ...utils.nms_utils import bb_intersection_over_union 
from ...utils.detector_utils import DetectorObject


__all__ = [
    'invert_affine',
    'aspectaware_resize_padding',
    'bbox_transform',
    'clip_boxes',
    'nms',
    'preprocess',
    'postprocess',
    'predictions_to_object'
]


def invert_affine(metas, preds):
    for i in range(len(preds)):
        if len(preds[i]['rois']) == 0:
            continue
        else:
            new_w, new_h, old_w, old_h, padding_w, padding_h = metas[i]
            preds[i]['rois'][:, [0, 2]] = preds[i]['rois'][:, [0, 2]] / (new_w / old_w)
            preds[i]['rois'][:, [1, 3]] = preds[i]['rois'][:, [1, 3]] / (new_h / old_h)

    return preds


def aspectaware_resize_padding(image, width, height, interpolation=None, means=None):
    old_h, old_w, c = image.shape
    if old_w > old_h:
        new_w = width
        new_h = int(width / old_w * old_h)
    else:
        new_w = int(height / old_h * old_w)
        new_h = height

    canvas = np.zeros((height, height, c), np.float32)
    if means is not None:
        canvas[...] = means

    if new_w != old_w or new_h != old_h:
        if interpolation is None:
            image = cv2.resize(image, (new_w, new_h))
        else:
            image = cv2.resize(image, (new_w, new_h), interpolation=interpolation)

    padding_h = height - new_h
    padding_w = width - new_w

    if c > 1:
        canvas[:new_h, :new_w] = image
    else:
        if len(image.shape) == 2:
            canvas[:new_h, :new_w, 0] = image
        else:
            canvas[:new_h, :new_w] = image

    return canvas, new_w, new_h, old_w, old_h, padding_w, padding_h


def bbox_transform(anchors, regression):
    """
    decode_box_outputs adapted from https://github.com/google/automl/blob/master/efficientdet/anchors.py
    Args:
        anchors: [batchsize, boxes, (y1, x1, y2, x2)]
        regression: [batchsize, boxes, (dy, dx, dh, dw)]
    Returns:
    """
    
    regression = np.array(regression, dtype=np.float128) ### overflow...
    
    y_centers_a = (anchors[..., 0] + anchors[..., 2]) / 2
    x_centers_a = (anchors[..., 1] + anchors[..., 3]) / 2
    ha = anchors[..., 2] - anchors[..., 0]
    wa = anchors[..., 3] - anchors[..., 1]

    w = np.exp(regression[..., 3]) * wa
    h = np.exp(regression[..., 2]) * ha

    y_centers = regression[..., 0] * ha + y_centers_a
    x_centers = regression[..., 1] * wa + x_centers_a

    ymin = y_centers - h / 2.
    xmin = x_centers - w / 2.
    ymax = y_centers + h / 2.
    xmax = x_centers + w / 2.

    return np.stack([xmin, ymin, xmax, ymax], axis=2)


def clip_boxes(boxes, img):
    _, _, height, width = img.shape

    boxes[:, :, 0] = np.clip(boxes[:, :, 0], 0, None)
    boxes[:, :, 1] = np.clip(boxes[:, :, 1], 0, None)
    boxes[:, :, 2] = np.clip(boxes[:, :, 2], None, width - 1)
    boxes[:, :, 3] = np.clip(boxes[:, :, 3], None, height - 1)

    return boxes


def nms(boxes, scores, iou_threshold):
    # remove overwrapped detection
    det = []
    keep = []
    for idx in range(len(boxes)):
        obj = boxes[idx]
        is_keep = True
        for idx2 in range(len(det)):
            if not keep[idx2]:
                continue
            box_a = [det[idx2][0], det[idx2][1], det[idx2][2], det[idx2][3]]
            box_b = [obj[0], obj[1], obj[2], obj[3]]
            iou = bb_intersection_over_union(box_a, box_b)
            if iou >= iou_threshold:
                if scores[idx2] <= scores[idx]:
                    keep[idx2] = False
                else:
                    is_keep = False
        det.append(obj)
        keep.append(is_keep)

    ret = []
    for _, idx in sorted(zip(scores, range(len(boxes))), reverse=True):
        if keep[idx]:
            ret.append(idx)

    return ret


def preprocess(img, input_size=512):
    mean = (0.406, 0.456, 0.485)
    std = (0.225, 0.224, 0.229)

    img = (img / 255 - mean) / std

    img_meta = aspectaware_resize_padding(
        img[..., ::-1], input_size, input_size, means=None)
    img = img_meta[0]
    framed_metas = img_meta[1:]

    img = img.transpose(2, 0, 1)
    img = np.expand_dims(img, axis=0)
    
    #img = np.ascontiguousarray(img, dtype=np.float32)
    
    return img, [framed_metas]


def postprocess(
        imgs,
        anchors, regression, classification,
        threshold, iou_threshold):
    transformed_anchors = bbox_transform(anchors, regression)
    transformed_anchors = clip_boxes(transformed_anchors, imgs)

    scores = np.max(classification, axis=2, keepdims=True)
    scores_over_thresh = (scores > threshold)[:, :, 0]

    out = []
    for i in range(imgs.shape[0]):
        if scores_over_thresh.sum() == 0:
            out.append({
                'rois': np.array(()),
                'class_ids': np.array(()),
                'scores': np.array(()),
            })

        classification_per = classification[i, scores_over_thresh[i, :], ...].transpose(1, 0)
        transformed_anchors_per = transformed_anchors[i, scores_over_thresh[i, :], ...]
        scores_per = scores[i, scores_over_thresh[i, :], ...]
        anchors_nms_idx = nms(transformed_anchors_per, scores_per[:, 0], iou_threshold=iou_threshold)

        if 0 < len(anchors_nms_idx):
            a = classification_per[:, anchors_nms_idx]
            scores_ = np.max(a, axis=0)
            classes_ = np.argmax(a, axis=0)
            boxes_ = transformed_anchors_per[anchors_nms_idx, :]
            out.append({
                'rois': boxes_,
                'class_ids': classes_,
                'scores': scores_,
            })
        else:
            out.append({
                'rois': np.array(()),
                'class_ids': np.array(()),
                'scores': np.array(()),
            })

    return out


def predictions_to_object(preds, w, h):
    i = 0
    detector_object = []
    for j in range(len(preds[i]['rois'])):
        (x1, y1, x2, y2) = preds[i]['rois'][j].astype(np.int)
        obj = preds[i]['class_ids'][j]
        score = float(preds[i]['scores'][j])

        r = DetectorObject(
            category=obj,
            prob=score,
            x=x1 / w,
            y=y1 / h,
            w=(x2 - x1) / w,
            h=(y2 - y1) / h,
        )

        detector_object.append(r)

    return detector_object