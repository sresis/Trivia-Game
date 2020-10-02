""" Data models for trivia game app. """
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


    def as_dict(self):
        return {
        'user_id': self.user_id,
        'username': self.username
        }

    def __repr__(self):
        return f'<user_id={self.user_id} username={self.username}>'

class Categories(db.Model):
    """A category."""

    __tablename__ = "categories"
    category_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    category_name = db.Column(db.String(50))
    def as_dict(self):
            return {
            'category_id': self.category_id,
            'category_name': self.category_name
            }

    def __repr__(self):
        return f'<category_id={self.category_id} category_name={self.category_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///trivia_game_db', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



if __name__ == '__main__':
    from server import app
    connect_to_db(app)