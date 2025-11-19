"""
Unit tests for the emotion detection application.
Tests the emotion_detector function with various inputs.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotion detection functionality.
    """
    
    def test_joy_emotion(self):
        """
        Test case for joy emotion detection.
        Statement: I am glad this happened
        Expected dominant emotion: joy
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger_emotion(self):
        """
        Test case for anger emotion detection.
        Statement: I am really mad about this
        Expected dominant emotion: anger
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_emotion(self):
        """
        Test case for disgust emotion detection.
        Statement: I feel disgusted just hearing about this
        Expected dominant emotion: disgust
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness_emotion(self):
        """
        Test case for sadness emotion detection.
        Statement: I am so sad about this
        Expected dominant emotion: sadness
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear_emotion(self):
        """
        Test case for fear emotion detection.
        Statement: I am really afraid that this will happen
        Expected dominant emotion: fear
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

