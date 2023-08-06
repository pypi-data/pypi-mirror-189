from openvino.inference_engine import IECore
from openvino.runtime import Core, Tensor
import numpy as np


class Openvino_multi:
    def __init__(self,model_path,**kwargs):
        self.xml_path = model_path
        
        self.core = Core()
        self.net = self.core.read_model(self.xml_path)
        
        # for infer
        self.compiled_model = self.core.compile_model(model=self.net, device_name="CPU")
        self.infer_request = self.compiled_model.create_infer_request()
        
        # output
        self.output_list = self.compiled_model.outputs
        output_names_ori = [list(o.get_names())[0] for o in self.output_list]

        self.sort_idx = np.array(range(len(output_names_ori)))
        self.output_names = output_names_ori
        self.weight = model_path.split('/')[-1].split('.')[-2]

    def run(self,img):
            
        input_tensor = Tensor(img)
        _ = self.infer_request.infer([input_tensor])
        
        
        output_tensors = []
        for i in self.sort_idx:
            output_tensors.append(self.infer_request.get_output_tensor(i))
        
        
        output = [ np.array(o.data) for o in output_tensors]
        
        return output

    def name(self):
        return self.weight