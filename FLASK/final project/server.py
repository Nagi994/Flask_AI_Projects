from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def analyze_emotion():
    """
    Analyze the emotion in the provided text and return the results in JSON format.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Handle cases where the dominant emotion is None
    if response['dominant_emotion'] is None:
        response = {"error": "Invalid text! Please try again."}
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)