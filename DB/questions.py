from model import db, Question, connect_to_db

def create_question(question_title, question_answer, incorrect_1,
incorrect_2, incorrect_3, question_difficulty, category_id):
    """Create and return a new question."""

    question = Question(question_title=question_title, question_answer=question_answer, incorrect_1=incorrect_1,
    incorrect_2=incorrect_2, incorrect_3=incorrect_3, question_difficulty=question_difficulty, category_id=category_id)

    db.session.add(question)
    db.session.commit()

    return question


def get_category_questions(category_id):
    """ Returns questions for a category ID."""
    category_questions = Question.query.filter(Question.category_id == category_id)

    print(category_questions)

get_category_questions(22)