# Import the necessary files
from ibm_watson import NaturalLanguageUnderstandingV1
from nltk.sentiment import SentimentIntensityAnalyzer

# Define the function
def emotion_detector(input_text):
    """Detects emotions in the provided input text."""
    #use a try catch block to catch any errors
    try:
        # Call the appropriate Emotion Detection library function
        detected_emotion = emotion_analysis_library.detect_emotion(input_text)
        return detected_emotion
    # If the try block does not work then it will throw an error
    except Exception as e:
        # Handle any errors that occur during detection
        return f"An error occurred: {e}"














