import sys
import os 
import glob
import subprocess
import torch

from ..models.efficientdet import efficientdet as effi
from ..models.yolov7 import yolov7 as yv7
from ..models.yolox import yolox as yx

from .load_onnx import Onnx_session
from .load_trt import load as Trt_load
from .load_vino import Openvino_multi


def check_gpu():
    cmd = "nvidia-smi --list-gpus"
    output = subprocess.check_output(cmd,shell=True)
    lines = output.decode().split('\n')
    lines = [ line.strip() for line in lines if line.strip() != '' ]

    return lines


class efficientdet:
    def __init__(self,model_type,model_path,**kwargs):

        self.model_path = model_path
        self.model_type = model_type
        self.onnx_device = kwargs.get('onnx_device','cuda')
        
        if self.model_type=='onnx':
            if self.onnx_device=='cuda' and len(check_gpu())==0:
                print("GPU Not Exists...")
                return None
            elif self.onnx_device=='cuda':
                print("Use GPU...")
            else:
                print("Use CPU...")
            self.net = Onnx_session(self.model_path,onnx_device=self.onnx_device)
            print("set onnx...")
        elif self.model_type=='v8.trt':
            if len(check_gpu())==0:
                print("GPU Not Exists...")
                return None
            else:
                print("GPU Ready...")
            torch.cuda.initialized = True
            torch.cuda.is_available()
            torch.cuda.set_device(0)
            self.net = Trt_load(self.model_path)
            print("set trt...")

        elif self.model_type=='openvino':
            self.net = Openvino_multi(self.model_path)
            print("set openvino...")
        else:
            print("check the model type...")

    def predict(self,input, check_eval, benchmark):

        if os.path.isdir(input):
            # Directory Path --> Generate "list" of inputs
            files_grapped = []
            in_dir = input
            for extension in ['*.png', '*.jpg', '*.[jJ][pP][eE][gG]', '*.bmp']:
                files_grapped.extend(glob.glob(os.path.join(in_dir, extension)))
            input = sorted(files_grapped)
        elif os.path.isfile(input):
            input = [input]
        else:
            print('specified input is not file path nor directory path')
            sys.exit(0)

        outs = []
        for image_path in input:
            out = effi.predict(image_path, self.net, self.model_type, check_eval, benchmark)
            outs.append(out)
        return outs
        
        
class yolox:
    def __init__(self,model_type,model_path,**kwargs):

        self.model_path = model_path
        self.model_type = model_type
        self.onnx_device = kwargs.get('onnx_device','cuda')

        if self.model_type=='onnx':
            if self.onnx_device=='cuda' and len(check_gpu())==0:
                print("GPU Not Exists...")
                return None
            elif self.onnx_device=='cuda':
                print("Use GPU...")
            else:
                print("Use CPU...")
                
            self.net = Onnx_session(self.model_path,onnx_device=self.onnx_device)
            print("set onnx...")
        elif self.model_type=='v8.trt':
            
            if len(check_gpu())==0:
                print("GPU Not Exists...")
                return None
            torch.cuda.initialized = True
            torch.cuda.is_available()
            torch.cuda.set_device(0)
            self.net = Trt_load(self.model_path)
            print("set trt...")
        elif self.model_type=='openvino':
            print("openvino")
            self.net = Openvino_multi(self.model_path)
            print("set openvino...")
    
    def predict(self,input, check_eval, benchmark):

        if os.path.isdir(input):
            # Directory Path --> Generate "list" of inputs
            files_grapped = []
            in_dir = input
            for extension in ['*.png', '*.jpg', '*.[jJ][pP][eE][gG]', '*.bmp']:
                files_grapped.extend(glob.glob(os.path.join(in_dir, extension)))
            input = sorted(files_grapped)
        elif os.path.isfile(input):
            input = [input]
        else:
            print('specified input is not file path nor directory path')
            sys.exit(0)

        outs = []
        for image_path in input:
            #print(image_path)
            out=yx.predict(image_path, self.net, self.model_type, check_eval, benchmark)
            outs.append(out)
        return outs

    
class yolov7:
    def __init__(self,model_type,model_path,**kwargs):

        self.model_path = model_path
        self.model_type = model_type
        self.onnx_device = kwargs.get('onnx_device','cuda')

        if self.model_type=='onnx':
            if self.onnx_device=='cuda' and len(check_gpu())==0:
                print("GPU Not Exists...")
                return None
            elif self.onnx_device=='cuda':
                print("Use GPU...")
            else:
                print("Use CPU...")
            self.net = Onnx_session(self.model_path,onnx_device=self.onnx_device)
            print("set onnx...")
        elif self.model_type=='v8.trt':
            if len(check_gpu())==0:
                print("GPU Not Exists...")
                return None
            torch.cuda.initialized = True
            torch.cuda.is_available()
            torch.cuda.set_device(0)
            self.net = Trt_load(self.model_path)
            print("set trt...")
        elif self.model_type=='openvino':
            self.net = Openvino_multi(self.model_path)
            print("set openvino...")
            
    def predict(self,input, check_eval, benchmark):

        if os.path.isdir(input):
            # Directory Path --> Generate "list" of inputs
            files_grapped = []
            in_dir = input
            for extension in ['*.png', '*.jpg', '*.[jJ][pP][eE][gG]', '*.bmp']:
                files_grapped.extend(glob.glob(os.path.join(in_dir, extension)))
            input = sorted(files_grapped)
        elif os.path.isfile(input):
            input = [input]
        else:
            print('specified input is not file path nor directory path')
            sys.exit(0)
        
        outs = []
        for image_path in input:
            out = yv7.predict(image_path, self.net, self.model_type, check_eval, benchmark)
            outs.append(out)
        return outs