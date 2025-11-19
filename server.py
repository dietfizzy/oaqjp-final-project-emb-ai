"""
Flask server for emotion detection web application.

This module provides a Flask web server that allows users to analyze
emotions in text using the Watson NLP library through a web interface.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the main page of the emotion detection application.

    This function serves the HTML template that provides the user interface
    for entering text to be analyzed for emotions.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint to detect emotions in the provided text.

    This function accepts GET requests with a 'textToAnalyze' query parameter,
    processes the text through the emotion detection service, and returns
    a formatted string response with emotion scores and dominant emotion.

    Returns:
        str: Formatted string response with emotion analysis results,
             or error message "Invalid text! Please try again!" if input
             is invalid or blank.

    Example:
        For input "I am happy", returns:
        "For the given statement, the system response is 'anger': 0.0,
         'disgust': 0.0, 'fear': 0.0, 'joy': 0.95 and 'sadness': 0.0.
         The dominant emotion is joy."
    """
    # Get text from query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Validate input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again."

    # Perform emotion detection
    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (error handling for blank entries)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the response as required
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

