class AnonumousSurvey():
    """Collecting anonymous responses to questions"""

    def __init__(self, question):
        """Save question and prepare for saving responses"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Displays the question."""
        print(self.question)

    def store_response(self, new_response):
        """Save one response to the question"""
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
