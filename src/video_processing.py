```python
import cv2
from src.object_detection import detect_objects

def process_video(video_file):
    # Initialize video capture object
    video = cv2.VideoCapture(video_file)

    # Check if video opened successfully
    if not video.isOpened():
        print("Error opening video file")
        return

    # Process video frame by frame
    while video.isOpened():
        # Capture frame-by-frame
        ret, frame = video.read()
        if ret:
            # Perform object detection on the frame
            detected_objects = detect_objects(frame)

            # Display the resulting frame with bounding boxes
            for obj in detected_objects:
                cv2.rectangle(frame, (obj['x'], obj['y']), (obj['x'] + obj['w'], obj['y'] + obj['h']), (0, 255, 0), 2)
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the video capture and close windows
    video.release()
    cv2.destroyAllWindows()
```