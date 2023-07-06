Shared Dependencies:

1. Exported Variables:
   - `video_file`: The uploaded video file.
   - `detected_objects`: The list of detected objects in the video.
   - `tracked_objects`: The list of tracked objects across video frames.
   - `null_objects`: The generated null objects for each detected object.

2. Data Schemas:
   - `ObjectSchema`: Schema for the detected objects, including properties like type, position, and orientation.
   - `NullObjectSchema`: Schema for the null objects, including properties like position and orientation.

3. DOM Element IDs:
   - `video-upload`: The file input element for video upload.
   - `video-processing`: The element displaying the video processing status.
   - `object-detection`: The element displaying the object detection results.
   - `object-tracking`: The element displaying the object tracking results.
   - `null-object-generation`: The element displaying the null object generation results.

4. Message Names:
   - `videoUploadSuccess`: Message indicating successful video upload.
   - `videoProcessingComplete`: Message indicating completion of video processing.
   - `objectDetectionComplete`: Message indicating completion of object detection.
   - `objectTrackingComplete`: Message indicating completion of object tracking.
   - `nullObjectGenerationComplete`: Message indicating completion of null object generation.

5. Function Names:
   - `uploadVideo()`: Function to handle video upload.
   - `processVideo()`: Function to process the uploaded video.
   - `detectObjects()`: Function to detect objects in the video.
   - `trackObjects()`: Function to track detected objects across video frames.
   - `generateNullObjects()`: Function to generate null objects for each detected object.