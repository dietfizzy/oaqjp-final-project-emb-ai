"""
Emotion detection module using Watson NLP library.
This module handles the core emotion detection functionality.
"""

import requests
import json
from typing import Dict, Any

def emotion_detector(text_to_analyze: str) -> Dict[str, Any]:
    """
    Analyzes the emotion in the given text using Watson NLP library.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions.
    
    Returns:
        dict: A dictionary containing emotion scores and dominant emotion.
              Format: {
                  'anger': float,
                  'disgust': float,
                  'fear': float,
                  'joy': float,
                  'sadness': float,
                  'dominant_emotion': str
              }
    
    Raises:
        Exception: If the API call fails or returns an error.
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'error': 'Invalid text! Please try again.'
        }
    
    # Watson NLP API endpoint (this would be configured in IBM Cloud)
    # In the IBM IDE, this would be the actual Watson NLP service URL
    url = 'https://sn-watson-emotion.labs.skills-network.net/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the API request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Input data for the API
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Make the API request
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse the response
            response_data = response.json()
            
            # Extract emotion predictions
            emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
            
            # Get emotion scores
            anger = emotions.get('anger', 0)
            disgust = emotions.get('disgust', 0)
            fear = emotions.get('fear', 0)
            joy = emotions.get('joy', 0)
            sadness = emotions.get('sadness', 0)
            
            # Find dominant emotion
            emotion_scores = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness
            }
            
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion,
                'emotions': emotion_scores
            }
        
        else:
            # Handle API errors
            return {
                'error': f'API request failed with status code {response.status_code}'
            }
    
    except requests.exceptions.Timeout:
        return {
            'error': 'Request timeout. Please try again.'
        }
    
    except requests.exceptions.ConnectionError:
        return {
            'error': 'Connection error. Please check your network connection.'
        }
    
    except requests.exceptions.RequestException as e:
        return {
            'error': f'Request failed: {str(e)}'
        }
    
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        return {
            'error': f'Error parsing response: {str(e)}'
        }
    
    except Exception as e:
        return {
            'error': f'Unexpected error: {str(e)}'
        }

