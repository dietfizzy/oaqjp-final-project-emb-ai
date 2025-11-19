# Emotion Detection Application

This is a Flask web application that uses IBM Watson NLP library to detect emotions in text. The application analyzes input text and returns emotion scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Features

- Emotion detection using Watson NLP library
- RESTful API endpoint for emotion analysis
- Web interface for easy interaction
- Comprehensive error handling
- Unit tests for validation
- Static code analysis support

## Project Structure

```
emotion_detection_app/
├── app.py                          # Main Flask application
├── EmotionDetection/
│   ├── __init__.py                 # Package initialization
│   └── emotion_detection.py       # Core emotion detection logic
├── templates/
│   └── index.html                  # HTML template for web interface
├── static/
│   └── style.css                   # CSS stylesheet
├── test_emotion_detection.py       # Unit tests
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup file
├── .pylintrc                       # Pylint configuration
├── .flake8                         # Flake8 configuration
├── .gitignore                      # Git ignore file
└── README.md                       # This file
```

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Install the package (optional):
```bash
pip install -e .
```

## Usage

### Running the Application

Start the Flask server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### API Endpoint

**POST /emotionDetector**

Analyzes emotions in the provided text.

**Request:**
- JSON: `{"textToAnalyze": "I am happy today"}`
- Form data: `textToAnalyze=I am happy today`

**Response:**
```json
{
    "anger": 0.0,
    "disgust": 0.0,
    "fear": 0.0,
    "joy": 0.95,
    "sadness": 0.0,
    "dominant_emotion": "joy"
}
```

### Web Interface

Navigate to `http://localhost:5000` in your browser to use the web interface. Enter text in the text area and click "Analyze Emotion" to see the results.

## Testing

Run the unit tests:
```bash
python -m pytest test_emotion_detection.py
```

Or using unittest:
```bash
python test_emotion_detection.py
```

## Static Code Analysis

### Pylint
```bash
pylint app.py EmotionDetection/ test_emotion_detection.py
```

### Flake8
```bash
flake8 app.py EmotionDetection/ test_emotion_detection.py
```

## Error Handling

The application includes comprehensive error handling for:
- Empty or invalid input
- API connection errors
- Timeout errors
- JSON parsing errors
- Unexpected exceptions

## Notes

- The Watson NLP API endpoint is configured for IBM Cloud environment
- In the IBM IDE, the API URL may need to be adjusted based on the actual service endpoint
- The application uses the `emotion_aggregated-workflow_lang_en_stock` model

## License

This project is part of an IBM course assignment.
