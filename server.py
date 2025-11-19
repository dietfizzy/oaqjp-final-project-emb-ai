"""
Flask server for emotion detection web application.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint to detect emotions in the provided text.
    Accepts GET requests with 'textToAnalyze' query parameter.
    
    Returns:
        Formatted string response with emotion analysis results.
    """
    # Get text from query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    # Validate input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again."
    
    # Perform emotion detection
    response = emotion_detector(text_to_analyze)
    
    # Check if response contains an error
    if 'error' in response:
        return f"Error: {response['error']}"
    
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

