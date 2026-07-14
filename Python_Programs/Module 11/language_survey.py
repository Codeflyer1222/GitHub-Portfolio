#!/usr/bin/env python3
#
# Problem: Develop a survey that queries partiticpants
#          to determine the 
# Files: 
#     language_survey.py (this file)
#     survey.py - AnonymousSurvey class definition
#     test_C11_anonSurveyClass.py - test functions
#
# Author: matthes (copied from text pg. 219)
# Date: 7 january 25
#
# import Survey
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()