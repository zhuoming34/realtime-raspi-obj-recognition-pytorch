"""
Camera module
"""
from numpy import ndarray
from cv2 import VideoCapture, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
from constants import WIDTH_RES, HEIGHT_RES, WIDTH_IMG, HEIGHT_IMG


def get_video() -> VideoCapture: 
    """
    Create a video capture object 
    """
    vid = VideoCapture(0)
    vid.set(CAP_PROP_FRAME_WIDTH, WIDTH_RES)
    vid.set(CAP_PROP_FRAME_HEIGHT, HEIGHT_RES)

    return vid


def center_square_img(
    frame, 
    width_old: int = WIDTH_RES,
    height_old: int = HEIGHT_RES,
    width_new: int = WIDTH_IMG, 
    height_new: int = HEIGHT_IMG
) -> ndarray:
    """
    Crop the image to be squared
    """
    assert frame
    assert width_old >= width_new > 0
    assert height_old >= height_new > 0

    h_start = int((height_old - height)/2)
    h_end = int((height_old + height)/2)
    w_start = int((width_old - width)/2)
    w_end = int((width_old + width)/2)

    img: ndarray = frame[h_start:h_end, w_start:w_end] 

    return img