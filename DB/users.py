from model import db, User

def create_user(username, password):
    """Create and return a new user."""

    user = User(username=username, password=password)

    db.session.add(user)
    db.session.commit()

    return user