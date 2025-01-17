import cv2
from torch import no_grad
from numpy import ndarray

from cam_utils import get_video, center_square_img
from pytorch_utils import network_init
from imagenet_utils import load_imagenet_labels, show_top_estimations
from constants import WIDTH_IMG


if __name__ == '__main__':

    # Initialization
    classes: dict = load_imagenet_labels()
    preprocessor, net = network_init()

    # Get a CV2 video capture object
    vid = get_video()

    # Check if the webcam is opened correctly
    if not vid.isOpened():
        raise IOError("Cannot open webcam")

    # Initial framerate value
    fps = 0

    # Run with no gradients
    with no_grad():
        while True: 
            # Get timestamp for calculating actual framerate
            timestamp = cv2.getTickCount()
        
            # Capture the video frame by frame
            ret: bool
            frame: ndarray 
            ret, frame = vid.read()
            if not ret:
                print("Cannot receive frames")
                break

            img = center_square_img(frame)
        
            # Convert opencv output from BRG to RGB
            # same as img_rgb = img[:, :, [2, 1, 0]]
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # preprocess
            input_tensor = preprocessor(img_rgb)

            # Create a mini-batch as expected by the model
            # the model can handle multiple images simultaneously 
            # so we add an extra dimension for the batch
            input_batch = input_tensor.unsqueeze(0)

            # Run model
            output = net(input_batch)

            # Print results
            top_one_est: str = show_top_estimations(output, classes)
            
            # Put top 1 estimation on frame
            cv2.putText(img,
                        top_one_est,
                        (0, WIDTH_IMG-10),
                        cv2.FONT_HERSHEY_PLAIN,
                        1,
                        (255, 255, 255))

            # Draw framerate on frame
            cv2.putText(img,
                        "FPS: " + str(round(fps, 2)),
                        (0, 12),
                        cv2.FONT_HERSHEY_PLAIN,
                        1,
                        (255, 255, 255))
                
            # Display the resulting frame
            cv2.imshow('frame', img)

            # Calculate framrate
            frame_time = (cv2.getTickCount() - timestamp) / cv2.getTickFrequency()
            fps = 1 / frame_time

            # the 'q' button is set as the quitting button you may use any 
            # desired button of your choice 
            pressed_key = cv2.waitKey(1) & 0xFF
            if pressed_key == ord('q'): 
                break
        
    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows() 
