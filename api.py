import requests
import os

#Base URL of all Open Trivia DB endpoints
BASE_URL = 'https://opentdb.com/api.php?'

def add_category_questions(category_id, question_count=50):
    """Returns category questions."""
  
    result = requests.get(BASE_URL + 'amount=' + str(question_count) + '&category=' + str(category_id) + '&type=multiple')
    api_result = result.json()
    question_info_list = []
    i = 0
    # add each question
    while i < question_count:
        question = api_result['results'][i]['question']
        correct_answer = api_result['results'][i]['correct_answer']
        incorrect_1 = api_result['results'][i]['incorrect_answers'][0]
        incorrect_2 = api_result['results'][i]['incorrect_answers'][1]
        incorrect_3 = api_result['results'][i]['incorrect_answers'][2]
        difficulty = api_result['results'][i]['difficulty']
         #make a dict to store the info
        category_info = {
        'question': question,
        'correct_answer': correct_answer,
        'incorrect_1': incorrect_1,
        'incorrect_2': incorrect_2,
        'incorrect_3': incorrect_3,
        'difficulty': difficulty,
        'category_id': category_id
        }
        question_info_list.append(category_info)
        i += 1


    return question_info_list


#add_category_questions(22, 50)