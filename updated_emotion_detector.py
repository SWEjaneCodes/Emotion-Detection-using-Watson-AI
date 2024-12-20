import watson_nlp  # Ensure watson_nlp is correctly imported

def emotion_detector(input_text):
    # Step 1: Load the pre-trained emotion detection model
    emotion_model = watson_nlp.load('emotion_transformer-workflow_multilingual_model')

    # Step 2: Run the model on the input text
    emotion_prediction = emotion_model.run(input_text, language_code="en")
    
    # Step 3: Extract individual emotion scores
    anger_score = emotion_prediction.get('emotion').get('anger', 0)
    disgust_score = emotion_prediction.get('emotion').get('disgust', 0)
    fear_score = emotion_prediction.get('emotion').get('fear', 0)
    joy_score = emotion_prediction.get('emotion').get('joy', 0)
    sadness_score = emotion_prediction.get('emotion').get('sadness', 0)

    # Step 4: Determine the dominant emotion
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    dominant_emotion = max(emotions, key=emotions.get)

    # Step 5: Format the output
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result
