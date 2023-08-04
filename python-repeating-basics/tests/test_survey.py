import unittest
from survey import AnonumousSurvey

class TestAnonumousSurvey(unittest.TestCase):
    """Tests for AnonumousSurvey class"""

    def setUp(self):
        """Creating survey and responses for all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonumousSurvey(question)
        self.responses = ['English', 'Czech', 'Deutsch']

    def test_store_single_response(self):
        """Check that single response is saved correctly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        """Check that single response is saved correctly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
