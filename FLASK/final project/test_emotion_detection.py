

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertIn('joy', result_1)

        result_2 = emotion_detector('I am really mad about this')
        self.assertIn('anger', result_2)

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertIn('disgust', result_3)

        result_4 = emotion_detector('I am so sad about this')
        self.assertIn('sadness', result_4)

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertIn('fear', result_5)

if __name__ == '__main__':
    unittest.main()       