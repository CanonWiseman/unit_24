from flask_sqlalchemy import SQLAlchemy
from app import bcrypt

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.model):
"""model for users"""

    __tablename__ = 'users'

    username = db.Column(db.String(20),
                        unique = True,
                        primary_key = True)

    password = db.Column(db.Text,
                        nullable = Fasle)

    email = db.Column(db.String(50),
                        unique = True,
                        nullable = False)

    first_name = db.Column(db.String(50),
                            nullable = False)

    last_name = db.Column(db.String(50),
                            nullable = False)

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """registers user with a hashed password"""

        hashed = bcrypt.generate_password_hash(pwd)

        hashed_uf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_uf8, email=email,first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False
