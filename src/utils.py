```python
import os
import cv2

def validate_video_file(video_file):
    """
    Validate the uploaded video file.
    """
    if not os.path.exists(video_file):
        raise FileNotFoundError(f"The video file {video_file} does not exist.")
    
    if not video_file.endswith(('.mp4', '.avi')):
        raise ValueError("Invalid video format. Only .mp4 and .avi formats are supported.")
    
    return True

def read_video(video_file):
    """
    Read the video file using OpenCV.
    """
    validate_video_file(video_file)
    video = cv2.VideoCapture(video_file)
    return video

def get_video_frames(video):
    """
    Get frames from the video.
    """
    frames = []
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)
    video.release()
    return frames

def write_jsx_file(null_objects, filename):
    """
    Write the null objects to a JSX file.
    """
    with open(filename, 'w') as file:
        file.write(str(null_objects))

def read_jsx_file(filename):
    """
    Read the null objects from a JSX file.
    """
    with open(filename, 'r') as file:
        null_objects = eval(file.read())
    return null_objects
```