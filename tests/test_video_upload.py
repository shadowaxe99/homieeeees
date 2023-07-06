```python
import unittest
from src import video_upload

class TestVideoUpload(unittest.TestCase):

    def setUp(self):
        self.video_file = "test_video.mp4"

    def test_upload_video(self):
        result = video_upload.uploadVideo(self.video_file)
        self.assertEqual(result, "videoUploadSuccess")

    def test_video_format(self):
        result = video_upload.checkVideoFormat(self.video_file)
        self.assertTrue(result)

    def test_large_video_file(self):
        result = video_upload.handleLargeVideoFile(self.video_file)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```