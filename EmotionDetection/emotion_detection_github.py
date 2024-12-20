import requests

# Define the function
def emotion_detector(input_text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { 
        "raw_document": { 
            "text": text_to_analyse 
        } 
    }
    """Detects emotions in the provided input text."""
    #use a try catch block to catch any errors
    try:
        # Call the appropriate Emotion Detection library function
        detected_emotion = requests.post(url, json=data, headers=headers, timeout=180)
        data_of_response = response.json()
        response = input_json['text']
        return response
    # If the try block does not work then it will throw an error
    except requests.exceptions.HTTPError as e:
        return f"An error occurred: {e}"

