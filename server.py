"""
Import all the necessary libraries
Catch any import errors using try catch block
Define the app
Defne the route
In the function we should
    1. Get input safely from the form by using the request.form.get() function
    2. Validate input using an if statement
    3. If statement to check for blank or empty values
    4. Pass the input to the emotion detection function by sendiing it the inp
from step 1
    5. Ensure the result is returned as a JSON dictionary by using jsonify() function
from flask

The root endpoint function catches any errors in the url
"""
from flask import Flask, request, jsonify

try:
    from EmotionDetection import emotion_detection
except ImportError as e:
    raise ImportError("EmotionDetection module not found or improperly configured.") from e

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detection_server():
    """
    Handles emotion detection by processing text input from a POST request.
    """
    inp = request.form.get("textarea", "").strip()
    if not inp:
        return jsonify({"error": "Input cannot be empty or blank."}), 400
    result = emotion_detection.emotion_detector(inp)
    if not isinstance(result, dict):
        return jsonify({"error": "Unexpected result format from emotion detection."}), 500
    return jsonify(result)

if __name__ == "__main__":
    # Run the Flask application locally with debugging enabled
    app.run(host="0.0.0.0", port=5000, debug=True)
