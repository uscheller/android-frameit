import unittest
from PIL import Image
from device_frame import DeviceFrame


class TranslationsTest(unittest.TestCase):
    def test_device_frame_boundaries(self):
        self.assertEqual(DeviceFrame("nexus5x").screen_boundaries(), (306, 485, 1386, 2405))
        self.assertEqual(DeviceFrame("nexus9").screen_boundaries(), (349, 514, 1885, 2562))
        self.assertEqual(DeviceFrame("pixelbook").screen_boundaries(), (381, 156, 1981, 2556))
        self.assertEqual(DeviceFrame("tablet1600x2560").screen_boundaries(), (300, 394, 1622, 2426))
        self.assertEqual(DeviceFrame("wear").screen_boundaries(), (201, 214, 521, 534))

    def test_device_frame_set_screen_shot(self):
        image = Image.open("example_screenshots/en_GB/screenshot_phone.png")
        DeviceFrame("nexus5x").set_screen_shot(image)


if __name__ == '__main__':
    unittest.main()
