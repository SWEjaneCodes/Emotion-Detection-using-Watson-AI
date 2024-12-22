import requests

def emotion_detector(input_text):
    """Detects emotions in the provided input text using Watson NLP."""
    
    # Define the API endpoint and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Format the input JSON
    input_json = {
        "raw_document": {
            "text": input_text
        }
    }
    
    try:
        # Make the POST request to the Watson API
        response = requests.post(url, json=input_json, headers=headers, timeout=30)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse the response JSON
        response_data = response.json()
        
        # Validate 'emotionPredictions' key
        if not response_data.get('emotionPredictions'):
            return {"error": "No emotion predictions found in the response"}
        
        # Access the first prediction and validate 'emotion'
        prediction = response_data['emotionPredictions'][0]
        emotion_scores = prediction.get('emotion', {})
        if not emotion_scores:
            return {"error": "No emotion scores found in the prediction"}
        
        # Extract individual emotion scores
        anger_score = emotion_scores.get('anger', 0)
        disgust_score = emotion_scores.get('disgust', 0)
        fear_score = emotion_scores.get('fear', 0)
        joy_score = emotion_scores.get('joy', 0)
        sadness_score = emotion_scores.get('sadness', 0)
        
        # Determine the dominant emotion
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
        }
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Format and return the output
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        return result
    
    except requests.exceptions.RequestException as e:
        # Log and return network or request error details
        return {"error": f"An HTTP request error occurred: {e}"}
    
    except Exception as e:
        # Catch-all for other unforeseen errors
        return {"error": f"An unexpected error occurred: {e}"}
