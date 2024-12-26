
"""
1. Get input safely from the form by using the request.form.get() function
2. Validate input using an if statement
3. If statement to check for blank or empty values
4. Pass the input to the emotion detection function by sendiing it the inp
from step 1
5. Ensure the result is returned as a JSON dictionary by using jsonify() function
from flask
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

# Define the app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detection_server():
    test_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection.emotion_detector(test_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."

    return response_text

@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint to guide users.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application locally with debugging enabled
    app.run(host="0.0.0.0", port=5000, debug=True)









