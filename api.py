import requests
import os

#Base URL of all Open Trivia DB endpoints
BASE_URL = 'https://opentdb.com/api.php?'

def get_category_question(category_id, question_count=1):
    """Returns a question given the category ID."""
    result = requests.get(BASE_URL + 'amount=' + str(question_count) + '&category=' + str(category_id))
    print(result.json())
    print('xx')
    return result.json()


get_category_question(22, 5)