import os
import unittest
from framed_image import FramedImage
from translations import Translations


class TranslationsTest(unittest.TestCase):
    def test_frame_image(self):
        """
        Just testing that it does not crash.
        """
        translations = Translations("default.json")
        screenshot = "example_screenshots/en_GB/screenshot_phone.png"
        root, file = os.path.dirname(screenshot), os.path.basename(screenshot)
        FramedImage(screen_shot=screenshot, output_name="should_not_be_saved.png") \
            .add_text(translations.get_title(root, file), translations.get_message(root, file),
                      title_font='fonts/MYRIADPRO-BOLDCOND.otf',
                      text_font='fonts/OpenSansCondensed-Light.ttf')


if __name__ == '__main__':
    unittest.main()
