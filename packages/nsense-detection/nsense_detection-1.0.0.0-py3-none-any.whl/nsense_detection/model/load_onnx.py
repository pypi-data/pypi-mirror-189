import cv2
import os
import numpy as np
import onnxruntime


class Onnx_session:
    def __init__(self,model_path,**kwargs):
        self.device = kwargs.get("onnx_device","cuda")
        if self.device=='cuda':
            self.providers= ['CUDAExecutionProvider']
        else:
            self.providers = ['CPUExecutionProvider']
        print("providers:",self.providers)
         
        self.net = onnxruntime.InferenceSession(model_path, providers=self.providers)
        self.input_name = self.net.get_inputs()[0].name
        self.output_names= [ output.name for output in self.net.get_outputs() ]
        self.outs_len = len(self.output_names)
        self.weight = model_path.split('/')[-1].split('.')[-2]

    def run(self,img):
        
        inp_dct = {self.input_name:img}
        outs = self.net.run(self.output_names, input_feed=inp_dct)

        return outs

    def name(self):
        return self.weight