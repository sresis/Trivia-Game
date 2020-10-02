from flask import (Flask, render_template, request, flash, session, jsonify,
				   redirect)
app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def root():
	"""view the homepage."""

	return render_template('root.html')



if __name__ == '__main__':
	connect_to_db(app)
	app.run()
	#app.run(host='0.0.0.0', debug=True)