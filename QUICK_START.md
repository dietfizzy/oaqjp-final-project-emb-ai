# Quick Start Guide

This guide will help you get started with the emotion detection application.

## Setup Instructions

### 1. Install Dependencies

In your terminal, navigate to the `emotion_detection_app` directory and run:

```bash
pip install -r requirements.txt
```

### 2. Run the Application

Start the Flask server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### 3. Test the Application

#### Using the Web Interface:
- Open your browser and go to `http://localhost:5000`
- Enter some text in the text area
- Click "Analyze Emotion"
- View the results

#### Using the API Endpoint:
You can test the API using curl:

```bash
curl -X POST http://localhost:5000/emotionDetector \
  -H "Content-Type: application/json" \
  -d '{"textToAnalyze": "I am happy today"}'
```

Or using Python:

```python
import requests

response = requests.post(
    'http://localhost:5000/emotionDetector',
    json={'textToAnalyze': 'I am happy today'}
)
print(response.json())
```

## Running Tests

Run the unit tests:

```bash
python test_emotion_detection.py
```

Or using pytest (if installed):

```bash
pytest test_emotion_detection.py
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

## Notes for IBM IDE

- The Watson NLP API endpoint is already configured in `EmotionDetection/emotion_detection.py`
- The URL `https://sn-watson-emotion.labs.skills-network.net/...` should work in the IBM IDE environment
- If you need to modify the API endpoint, edit the `url` variable in `EmotionDetection/emotion_detection.py`

## Project Tasks Checklist

- [x] Task 1: Fork and Clone the project repository
- [x] Task 2: Create an emotion detection application using Watson NLP library
- [x] Task 3: Format the output of the application
- [x] Task 4: Package the application
- [x] Task 5: Run Unit tests on your application
- [x] Task 6: Deploy as web application using Flask
- [x] Task 7: Incorporate Error handling
- [x] Task 8: Run static code analysis

## File Descriptions

- **app.py**: Main Flask application with routes
- **EmotionDetection/emotion_detection.py**: Core emotion detection logic using Watson NLP
- **templates/index.html**: Web interface HTML template
- **static/style.css**: CSS styling for the web interface
- **test_emotion_detection.py**: Unit tests for the application
- **requirements.txt**: Python package dependencies
- **setup.py**: Package installation configuration

