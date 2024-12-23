# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square' and 'double' functions from the 'mymodule' module.
from emotion_detection_github import emotion_detector


# Define a test case class for testing the 'double' function.
class TestEmotionDetector(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self):
        self.assertEqual(emotion_detector("I am really glad this happened"), "joy") # test when "I am really glad this happened" is given as input the output is "joy".
        self.assertEqual(emotion_detector("I am really mad about this"), "anger") # test when "I am really mad about this" is given as input the output is "anger".
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this"), "disgust") # test when "I feel disgusted just hearing about this" is given as input the output is "disgust".
        self.assertEqual(emotion_detector("I am so sad about this"), "sadness") # test when "I am so sad about this" is given as input the output is "sadness".
        self.assertEqual(emotion_detector("I am really afraid that this will happen"), "fear") # test when "I am really afraid that this will happen" is given as input the output is "fear".
        
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()
