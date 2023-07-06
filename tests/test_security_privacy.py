```python
import unittest
from src import security_privacy

class TestSecurityPrivacy(unittest.TestCase):

    def setUp(self):
        self.security_privacy = security_privacy.SecurityPrivacy()

    def test_video_encryption(self):
        video_file = 'test_video.mp4'
        self.security_privacy.encrypt_video(video_file)
        self.assertTrue(self.security_privacy.is_encrypted(video_file))

    def test_video_decryption(self):
        video_file = 'test_video.mp4'
        self.security_privacy.encrypt_video(video_file)
        self.security_privacy.decrypt_video(video_file)
        self.assertFalse(self.security_privacy.is_encrypted(video_file))

    def test_user_data_protection(self):
        user_data = {'name': 'Test User', 'email': 'testuser@example.com'}
        self.security_privacy.protect_user_data(user_data)
        self.assertTrue(self.security_privacy.is_protected(user_data))

if __name__ == '__main__':
    unittest.main()
```