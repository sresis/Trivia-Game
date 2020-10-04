import requests
import os

#Base URL of all Open Trivia DB endpoints
BASE_URL = 'https://opentdb.com/api.php?'

def get_category_question(category_id, question_count=1):
    """Returns a question given the category ID."""
    result = requests.get(BASE_URL + 'amount=' + str(question_count) + '&category=' + str(category_id))
    api_result = result.json()
    print('*******')
    print(api_result['results'][0]['question'])
    question = api_result['results'][0]['question']
    correct_answer = api_result['results'][0]['correct_answer']
    incorrect_answers = api_result['results'][0]['incorrect_answers']
    difficulty = api_result['results'][0]['difficulty']
    
    #make a dict to store the info
    category_info = {
        'question': question,
        'correct_answer': correct_answer,
        'incorrect_answers': incorrect_answers,
        'difficulty': difficulty
    }
    print(category_info)


    return category_info


#get_category_question(22)