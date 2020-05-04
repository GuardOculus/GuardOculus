from app.models import User
from app import db

def test_get_user_by_username(app):
    """Ensure that user can be got from database by username"""
    user = User(username="toaster", role=1)
    user.set_password("toaster")

    db.session.add(user)
    db.session.commit()

    user_from_database = User.query.filter_by(username="toaster").first()

    assert user_from_database == user


def test_check_password(app):
    """Ensure that password matching by hash works"""
    user = User(username="toaster", role=1)
    user.set_password("toaster")

    assert user.check_password("toaster") == True
    assert user.check_password("password") == False
