```python
import unittest
from src.object_detection import detectObjects

class TestObjectDetection(unittest.TestCase):

    def setUp(self):
        self.video_file = "test_video.mp4"
        self.detected_objects = []

    def test_detect_objects(self):
        self.detected_objects = detectObjects(self.video_file)
        self.assertIsNotNone(self.detected_objects, "No objects detected.")
        for obj in self.detected_objects:
            self.assertIn('type', obj, "Object type not found.")
            self.assertIn('position', obj, "Object position not found.")
            self.assertIn('orientation', obj, "Object orientation not found.")

if __name__ == '__main__':
    unittest.main()
```