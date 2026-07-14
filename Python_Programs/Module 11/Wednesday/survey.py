#!/usr/bin/env python3
#
# Problem: C11 Test class example
#
# Files: 
#     survey.py (this file)
#     language_survey.py - main program module
#     test_C11_anonSurveyClass.py - test functions
#
# # Author: matthes (copied from text pg. 218)
# Date: 7 january 25
#
# import class to be tested
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")