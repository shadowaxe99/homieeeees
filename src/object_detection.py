```python
import cv2
from yolov7 import YOLOv7

# Define the object detection function
def detect_objects(video_file):
    # Initialize YOLOv7
    yolo = YOLOv7()

    # Load the video
    video = cv2.VideoCapture(video_file)

    # Initialize the list of detected objects
    detected_objects = []

    # Loop over the frames from the video stream
    while True:
        # Read the next frame from the file
        (grabbed, frame) = video.read()

        # If the frame was not grabbed, then we have reached the end of the stream
        if not grabbed:
            break

        # Detect objects in the frame and append to the list
        objects = yolo.detect(frame)
        detected_objects.extend(objects)

    # Release the file pointers
    video.release()

    # Return the list of detected objects
    return detected_objects
```