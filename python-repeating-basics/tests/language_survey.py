from survey import AnonumousSurvey

# Determining the question with creating an instance of AnonymousSurvey.
question = "What language did you first learn to speak?"

my_survey = AnonumousSurvey(question)

# Display question and saving the responses.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response.title())

# Display the results.
print("Thank you to everyone who participated in the survey!")
my_survey.show_results()
