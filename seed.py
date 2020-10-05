""" Script to seed database."""

import os
import json
import model
import server
import api
from DB import categories, users, questions


os.system('dropdb trivia_game_db')
os.system('createdb trivia_game_db')

model.connect_to_db(server.app)
model.db.create_all()

category_list = [['Animals', 27], ['Geography', 22], ['Sports', 21]]

# add categories to DB
for item in category_list:
    #verify that it isn't already in DB
    if categories.get_category(item[0]) == None:
        categories.create_category(item[0], item[1])

# add questions to DB
# get list of question info for each category
for item in category_list:
    category_id = item[1]
    category_questions = api.add_category_questions(category_id)

    # add each question to db
    for question in category_questions:
        # get question details
        question_title = question['question']
        correct_answer = question['correct_answer']
        incorrect_1 = question['incorrect_1']
        incorrect_2 = question['incorrect_2']
        incorrect_3 = question['incorrect_3']
        difficulty = question['difficulty']

        #add it to DB
        new_ques = questions.create_question(question_title, correct_answer, incorrect_1,
        incorrect_2, incorrect_3, difficulty, category_id)





