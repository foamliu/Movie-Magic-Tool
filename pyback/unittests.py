import unittest
import numpy as np

from common import parse_scenedetect_result

class TestMethods(unittest.TestCase):
    def test_parse_scenedetect_result(self):
        result = """[PySceneDetect] Detecting scenes (content mode)...
[PySceneDetect] Parsing video Game_Of_Hunting_EP1_new.mp4...
[PySceneDetect] Video Resolution / Framerate: 1920 x 1080 / 24.000 FPS
Verify that the above parameters are correct (especially framerate, use --force-fps to correct if required).
[PySceneDetect] Current Processing Speed: 12.1 FPS
[PySceneDetect] Current Processing Speed: 12.2 FPS
[PySceneDetect] Current Processing Speed: 12.3 FPS
[PySceneDetect] Current Processing Speed: 12.3 FPS
[PySceneDetect] Current Processing Speed: 12.3 FPS
[PySceneDetect] Current Processing Speed: 12.0 FPS
[PySceneDetect] Current Processing Speed: 12.5 FPS
[PySceneDetect] Current Processing Speed: 12.5 FPS
[PySceneDetect] Current Processing Speed: 12.1 FPS
[PySceneDetect] Current Processing Speed: 12.4 FPS
[PySceneDetect] Processing complete, found 13 scenes in video.
[PySceneDetect] Processed 1248 / 1248 frames read in 101.8 secs (avg 12.3 FPS).
[PySceneDetect] Comma-separated timecode output:
00:00:03.250,00:00:04.291,00:00:07.750,00:00:13.375,00:00:16.541,00:00:22.333,00:00:27.333,00:00:31.125,00:00:33.583,00:00:35.958,00:00:46.375,00:00:48.500,00:00:50.083"""

        actual = parse_scenedetect_result(result)
        expect = [3.25, 4.291, 7.75, 13.375, 16.541, 22.333, 27.333, 31.125, 33.583, 35.958, 46.375, 48.5, 50.083]

        self.assertEqual(np.allclose(actual, expect, rtol=1e-05, atol=1e-08), True)

if __name__ == '__main__':
    unittest.main()