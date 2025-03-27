# tests/test_resume.py
import unittest
from app import cleanResume, pred  # Replace "your_script_name" with the name of your Python file (e.g., "app")

class TestResumeProcessing(unittest.TestCase):
    def test_cleanResume(self):
        # Test if URLs, mentions, and hashtags are removed
        sample_text = "Check @user https://example.com #hashtag"
        cleaned = cleanResume(sample_text)
        self.assertNotIn("@user", cleaned)
        self.assertNotIn("https://example.com", cleaned)
        self.assertNotIn("#hashtag", cleaned)

    def test_pred(self):
        # Test if prediction returns a valid category
        sample_resume = "Experienced software engineer with Python skills"
        category = pred(sample_resume)
        self.assertIsInstance(category, str)  # Ensure output is a string
        self.assertNotEqual(category, "")  # Ensure category is not empty

if __name__ == "__main__":
    unittest.main()