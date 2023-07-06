```python
import unittest
from src import documentation_support

class TestDocumentationSupport(unittest.TestCase):

    def setUp(self):
        self.documentation = documentation_support.DocumentationSupport()

    def test_setup_instructions(self):
        instructions = self.documentation.get_setup_instructions()
        self.assertIsInstance(instructions, str)
        self.assertGreater(len(instructions), 0)

    def test_usage_guidelines(self):
        guidelines = self.documentation.get_usage_guidelines()
        self.assertIsInstance(guidelines, str)
        self.assertGreater(len(guidelines), 0)

    def test_support_channels(self):
        channels = self.documentation.get_support_channels()
        self.assertIsInstance(channels, dict)
        self.assertIn('email', channels)
        self.assertIn('live_chat', channels)

if __name__ == '__main__':
    unittest.main()
```