"""
Server module for the NLP Emotion Detection application.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page where the user can input text for analysis.
    :return: Rendered HTML template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handle GET requests to analyze the given text for emotions.
    :return: JSON response containing emotion analysis or error message.
    """
    try:
        # Get the 'textToAnalyze' query parameter from the URL
        text_to_analyse = request.args.get('textToAnalyze', '')

        # Use the emotion_detector function
        result = emotion_detector(text_to_analyse)

        # Check for invalid inputs or server errors
        if result['dominant_emotion'] is None:
            response_text = "Invalid text! Please try again!"
            return jsonify({"response": response_text}), 400

        # Format the response
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}."
            f" The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify({"response": response_text}), 200

    except ValueError as error:
        return jsonify({"error": f"Value Error: {str(error)}"}), 500
    except KeyError as error:
        return jsonify({"error": f"Key Error: {str(error)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
