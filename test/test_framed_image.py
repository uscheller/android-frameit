import unittest
from framed_image import FramedImage


class TranslationsTest(unittest.TestCase):
    def test_frame_image(self):
        """
        Just testing that it does not crash.
        """
        screenshot = "example_screenshots/en_GB/screenshot_phone.png"
        FramedImage(screen_shot=screenshot, output_name="should_not_be_saved.png")


if __name__ == '__main__':
    unittest.main()
