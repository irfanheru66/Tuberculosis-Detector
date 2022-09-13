from PIL import Image
import torch
import time


def process(img,conf_level,iou):
    model = torch.hub.load('WongKinYiu/yolov7', 'custom', path_or_model='best.pt',)

    print(conf_level)
    model.conf = conf_level
    model.iou = iou  
    model.cpu()
    since = time.time()
    pred = model(img)
    pred.render()
    runtime = f'Inference complete { (time.time()-since)*1000:.5f}ms'

    im_base64 = Image.fromarray(pred.imgs[0])
    return im_base64,len(pred.xyxyn[0][:, -1].numpy()),runtime

