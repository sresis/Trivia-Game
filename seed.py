""" Script to seed database."""

import os
import json
import model
import server
from DB import categories, users


os.system('dropdb trivia_game_db')
os.system('createdb trivia_game_db')

model.connect_to_db(server.app)
model.db.create_all()

category_list = [['Animals', 27], ['Geography', 22], ['Sports', 21]]

for item in category_list:
    #verify that it isn't already in DB
    if categories.get_category(item[0]) == None:
        categories.create_category(item[0], item[1])

