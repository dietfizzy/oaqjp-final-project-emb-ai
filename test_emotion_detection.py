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
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger_emotion(self):
        """
        Test case for anger emotion detection.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_emotion(self):
        """
        Test case for disgust emotion detection.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness_emotion(self):
        """
        Test case for sadness emotion detection.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear_emotion(self):
        """
        Test case for fear emotion detection.
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_empty_string(self):
        """
        Test case for empty string input.
        """
        result = emotion_detector("")
        self.assertIn('error', result)
    
    def test_whitespace_string(self):
        """
        Test case for whitespace-only input.
        """
        result = emotion_detector("   ")
        self.assertIn('error', result)
    
    def test_emotion_scores_format(self):
        """
        Test case to verify emotion scores are in correct format.
        """
        result = emotion_detector("I am happy")
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
        
        # Check that scores are numeric
        self.assertIsInstance(result['anger'], (int, float))
        self.assertIsInstance(result['disgust'], (int, float))
        self.assertIsInstance(result['fear'], (int, float))
        self.assertIsInstance(result['joy'], (int, float))
        self.assertIsInstance(result['sadness'], (int, float))

if __name__ == '__main__':
    unittest.main()

