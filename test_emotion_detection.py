from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertGreater(result_1['joy'], 0.5)

        result_2 = emotion_detector('I am really mad about this')
        self.assertGreater(result_2['anger'], 0.5)

        result_3 = emotion_detector('I am so sad about this')
        self.assertGreater(result_3['sadness'], 0.5)

        result_4 = emotion_detector('I feel disgusted just hearing about this')
        self.assertGreater(result_4['disgust'], 0.5)

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertGreater(result_5['fear'], 0.5)
        
if __name__ == '__main__':
    unittest.main()