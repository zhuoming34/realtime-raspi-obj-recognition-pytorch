"""
Constants
"""

# Camera settings
WIDTH_RES = 640
HEIGHT_RES = 360
WIDTH_IMG = 224
HEIGHT_IMG = WIDTH_IMG

# PyTorch settings
BACKEND_ENGIN = 'qnnpack'
IMG_NORMALIZE_MEAN = (0.485, 0.456, 0.406)
IMG_NORMALIZE_STD = (0.229, 0.224, 0.225)

# Labels for 1000 classes
IMAGENET_LABEL_FILE = "imagenet1000_clsidx_to_labels.json"
