"""
Utils for PyTorch operations
"""
import torch
from torchvision.transforms import Compose, ToTensor, Normalize
from torchvision.models.quantization import mobilenet_v3_large, MobileNet_V3_Large_QuantizedWeights
from constants import BACKEND_ENGIN, IMG_NORMALIZE_MEAN, IMG_NORMALIZE_STD


def get_preprocessor() -> Compose:
    
    return Compose([
        # convert the frame to a CHW torch tensor for training
        ToTensor(),
        # normalize the colors to the range that mobilenet_v2/3 expect
        Normalize(mean=IMG_NORMALIZE_MEAN, std=IMG_NORMALIZE_STD),
        ])


def get_model():

    # MobileNet mobile
    net = mobilenet_v3_large(weights=MobileNet_V3_Large_QuantizedWeights.DEFAULT, quantize=True)

    # JIT the model to reduce Python overhead and fuse any ops
    net = torch.jit.script(net)

    return net


def network_init():
    # The aarch64 version of pytorch requires using the qnnpack engine
    torch.backends.quantized.engine = BACKEND_ENGIN
    preprocessor = get_preprocessor()
    net = get_model()

    return preprocessor, net
