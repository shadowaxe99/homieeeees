```python
import unittest
from unittest.mock import patch
from src import user_interface

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.uploadVideo')
    def test_uploadVideo(self, mock_upload):
        mock_upload.return_value = 'videoUploadSuccess'
        response = user_interface.uploadVideo('test_video.mp4')
        self.assertEqual(response, 'videoUploadSuccess')

    @patch('src.user_interface.processVideo')
    def test_processVideo(self, mock_process):
        mock_process.return_value = 'videoProcessingComplete'
        response = user_interface.processVideo('test_video.mp4')
        self.assertEqual(response, 'videoProcessingComplete')

    @patch('src.user_interface.detectObjects')
    def test_detectObjects(self, mock_detect):
        mock_detect.return_value = 'objectDetectionComplete'
        response = user_interface.detectObjects('test_video.mp4')
        self.assertEqual(response, 'objectDetectionComplete')

    @patch('src.user_interface.trackObjects')
    def test_trackObjects(self, mock_track):
        mock_track.return_value = 'objectTrackingComplete'
        response = user_interface.trackObjects('test_video.mp4')
        self.assertEqual(response, 'objectTrackingComplete')

    @patch('src.user_interface.generateNullObjects')
    def test_generateNullObjects(self, mock_generate):
        mock_generate.return_value = 'nullObjectGenerationComplete'
        response = user_interface.generateNullObjects('test_video.mp4')
        self.assertEqual(response, 'nullObjectGenerationComplete')

if __name__ == '__main__':
    unittest.main()
```