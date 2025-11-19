"""
Flask application for emotion detection using Watson NLP library.
This is the main application file that handles HTTP requests.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Endpoint to detect emotions in the provided text.
    Accepts POST requests with JSON or form data containing 'textToAnalyze'.
    
    Returns:
        JSON response with emotion analysis results or error message.
    """
    try:
        # Get text from request
        if request.is_json:
            data = request.get_json()
            text_to_analyze = data.get('textToAnalyze', '')
        else:
            text_to_analyze = request.form.get('textToAnalyze', '')
        
        # Validate input
        if not text_to_analyze or not text_to_analyze.strip():
            return jsonify({
                "error": "Invalid text! Please try again."
            }), 400
        
        # Perform emotion detection
        response = emotion_detector(text_to_analyze)
        
        # Check if response contains an error
        if 'error' in response:
            return jsonify(response), 400
        
        # Format the response
        dominant_emotion = response.get('dominant_emotion')
        emotions = response.get('emotions', {})
        
        # Create formatted output
        formatted_response = {
            "anger": emotions.get('anger', 0),
            "disgust": emotions.get('disgust', 0),
            "fear": emotions.get('fear', 0),
            "joy": emotions.get('joy', 0),
            "sadness": emotions.get('sadness', 0),
            "dominant_emotion": dominant_emotion
        }
        
        return jsonify(formatted_response)
    
    except Exception as e:
        return jsonify({
            "error": f"An error occurred: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

