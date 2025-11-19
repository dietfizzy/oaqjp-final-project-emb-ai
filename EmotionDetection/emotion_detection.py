"""
Emotion detection function using Watson NLP library.
"""

import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion in the given text using Watson NLP library.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions.
    
    Returns:
        dict: Formatted dictionary with emotion scores and dominant emotion.
    """
    # Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the API request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input data for the API
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Make the API request
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the required set of emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (emotion with the highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

