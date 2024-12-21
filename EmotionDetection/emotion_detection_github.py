import requests

def emotion_detector(input_text):
    """Detects the dominant emotion in the provided input text."""
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { 
        "raw_document": { 
            "text": input_text  # Use input_text as the source for analysis
        } 
    }
    
    try:
        # Call the Watson NLP Emotion Detection API
        response = requests.post(url, json=input_json, headers=headers, timeout=180)
        response.raise_for_status()  # Raise HTTPError if the response status indicates an error
        
        # Parse the response JSON
        data_of_response = response.json()
        
        # Extract emotion scores (adjust if the structure is different)
        emotion_scores = data_of_response.get("document", {}).get("emotion", {})
        if not isinstance(emotion_scores, dict) or not emotion_scores:
            return "No emotions detected or unexpected response format."
        
        # Determine the dominant emotion based on the highest score
        max_score = float('-inf')
        dominant_emotion = None

        # Loop through the dictionary to find the max score
        for emotion, score in emotion_scores.items():
            if score > max_score:
                max_score = score
                dominant_emotion = emotion
        
        return f"The dominant emotion is '{dominant_emotion}' with a score of {max_score:.2f}."
        
    except requests.exceptions.RequestException as e:
        # Handle network or request errors
        return f"An error occurred: {e}"

