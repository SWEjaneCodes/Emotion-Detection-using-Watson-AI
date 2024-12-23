from flask import Flask, request, jsonify

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detection_server():
    if request.method == "POST":
        # Get input safely from the form
        inp = request.form.get("textarea", "")

        # Pass the input to the emotion detection function
        result = emotion_detection.emotion_detector(inp)
        
        # Ensure the result is returned as a JSON dictionary
        return jsonify(result), 200
    
    # If GET request is accidentally made
    return jsonify({"error": "Use POST method to access this endpoint."}), 405

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
