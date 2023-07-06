```python
import unittest
from src import video_processing

class TestVideoProcessing(unittest.TestCase):

    def setUp(self):
        self.video_file = "test_video.mp4"
        self.processed_video = video_processing.processVideo(self.video_file)

    def test_video_processing(self):
        self.assertIsNotNone(self.processed_video, "Video processing failed.")

    def test_video_format(self):
        self.assertTrue(self.processed_video.endswith('.mp4'), "Processed video is not in MP4 format.")

    def test_large_video_file(self):
        self.assertLessEqual(self.processed_video.size, 5000000, "Processed video file size is too large.")

if __name__ == '__main__':
    unittest.main()
```