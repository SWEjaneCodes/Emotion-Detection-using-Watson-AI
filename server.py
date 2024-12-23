# Import all the necessary libraries
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detection

# Define app
app = Flask("Emotion Detector")

# Define the route 
@app.route("/emotionDetector", methods=["POST"])
def emotion_detection_server():
    if request.method == "POST":
        """
        1. Get input safely from the form by using the request.form.get() function
        2. Validate input using an if statement
        3. Pass the input to the emotion detection function by sendiing it the inp
        from step 1
        4. Ensure the result is returned as a JSON dictionary by using jsonify() function
        from flaask
        """
        inp = request.form.get("textarea", "")
        if not inp.strip():
            return jsonify({"error": "Please provide valid input in the textarea."}), 400
        result = emotion_detection.emotion_detector(inp)
        return jsonify(result)
    # If GET request is accidentally made
    return jsonify({"error": "Use POST method to access this endpoint."}), 405

if __name__ == "__main__":
    #make sure we are accessing port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)




