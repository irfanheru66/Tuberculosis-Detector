from PIL import Image
import torch
import time


def process(img,conf_level,iou):
    since = time.time()
    model = torch.hub.load('WongKinYiu/yolov7', 'custom', path_or_model='best.pt',)

    model.conf = conf_level
    model.iou = iou  
    model.cpu()
    pred = model(img)

    pred.render()
    im_base64 = Image.fromarray(pred.imgs[0])
    runtime = f'Total Inference time: { (time.time()-since)*1000:.2f}ms'
    return im_base64,len(pred.xyxyn[0][:, -1].numpy()),runtime

