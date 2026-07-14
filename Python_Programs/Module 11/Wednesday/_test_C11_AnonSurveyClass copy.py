#!/usr/bin/env python3
#
# Problem: C11 Test class example
# Files: 
#     test_C11_anonSurveyClass.py (this file)
#     survey.py - AnonymousSurvey class definition
#     language_survey.py - main program module
#
# Author: matthes (copied from text pg. 220, 221)
# Date: 7 january 25
#
# import class to be tested
from survey import AnonymousSurvey

# define atribute definition test function
def test_survey_creation ():
    """Test that a single response is stored properly."""
    question = "What langauge did you first learn to speak?"
    language_survey = AnonymousSurvey (question)
    assert language_survey.question == question

# define class test function
def test_store_single_response ():
    """Test that a single response is stored properly."""
    question = "What langauge did you first learn to speak?"
    language_survey = AnonymousSurvey (question)
    language_survey.store_response ('English')
    assert 'English' in language_survey.responses

def test_store_three_response ():
    """ the code below is for three entries """
    question = "What langauge did you first learn to speak?"
    language_survey = AnonymousSurvey (question)
    responses = ['English', 'Spanish', 'Mandrain']
    for response in responses:
        language_survey.store_response (response)
    
    for response in responses:
        assert response in language_survey.responses

