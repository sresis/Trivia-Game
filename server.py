from flask import (Flask, render_template, request, flash, session, jsonify,
				   redirect)
from model import connect_to_db, Category, User
from jinja2 import StrictUndefined
from DB import categories
import api


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def root():
	"""view the homepage."""

	return render_template('root.html')

@app.route('/api/categories')
def get_categories():
    """ View all categories."""

    all_categories = categories.get_all_categories()
    # store info then jsonify
    category_list = []
    for category in all_categories:
        category_item = Category.as_dict(category)
        category_list.append(category_item)

    


    
    return jsonify(category_list)

@app.route('/api/category/<api_id>', methods=['POST'])
def get_question(api_id):
    """Returns a question in the selected category."""
    question_info = api.get_category_question(api_id)
    print(question_info)
    return jsonify(question_info)
    




if __name__ == '__main__':
	connect_to_db(app)
	app.run(host='0.0.0.0', debug=True)