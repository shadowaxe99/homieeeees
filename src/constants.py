```python
# src/constants.py

# DOM Element IDs
VIDEO_UPLOAD = 'video-upload'
VIDEO_PROCESSING = 'video-processing'
OBJECT_DETECTION = 'object-detection'
OBJECT_TRACKING = 'object-tracking'
NULL_OBJECT_GENERATION = 'null-object-generation'

# Message Names
VIDEO_UPLOAD_SUCCESS = 'videoUploadSuccess'
VIDEO_PROCESSING_COMPLETE = 'videoProcessingComplete'
OBJECT_DETECTION_COMPLETE = 'objectDetectionComplete'
OBJECT_TRACKING_COMPLETE = 'objectTrackingComplete'
NULL_OBJECT_GENERATION_COMPLETE = 'nullObjectGenerationComplete'

# Function Names
UPLOAD_VIDEO = 'uploadVideo'
PROCESS_VIDEO = 'processVideo'
DETECT_OBJECTS = 'detectObjects'
TRACK_OBJECTS = 'trackObjects'
GENERATE_NULL_OBJECTS = 'generateNullObjects'

# Supported video formats
SUPPORTED_VIDEO_FORMATS = ['mp4', 'avi']

# YOLOv7 configuration
YOLOV7_CONFIG = {
    'weights_path': 'yolov7.weights',
    'cfg_path': 'yolov7.cfg',
    'names_path': 'yolov7.names'
}

# Tracking algorithms
TRACKING_ALGORITHMS = ['kalman', 'correlation']

# Adobe After Effects JSX file configuration
JSX_FILE_CONFIG = {
    'file_extension': '.jsx',
    'null_object_template': 'NullObjectTemplate.jsx'
}
```