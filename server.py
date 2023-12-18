from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

def emotion_analyzer(text_to_analyze):
    """This function calls the application"""
    emotion_result = emotion_detector(text_to_analyze)

    if emotion_result['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {emotion_result['anger']}, "
            f"'disgust': {emotion_result['disgust']}, 'fear': {emotion_result['fear']}, "
            f"'joy': {emotion_result['joy']} and 'sadness': {emotion_result['sadness']}. "
            f"The dominant emotion is {emotion_result['dominant_emotion']}.")

    return response_text

@app.route("/")
def render_index_page():
    """Renders the index page."""
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def evaluate_emotion():
    """Route for emotion analyzer."""
    text_to_analyze = request.args.get('textToAnalyze')
    response_text = emotion_analyzer(text_to_analyze)
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

