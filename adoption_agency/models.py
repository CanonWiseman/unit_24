from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

#models go here

class Pet(db.Model):
    """Pet model"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True,
                   nullable = False)

    name = db.Column(db.String(50),
                    nullable = False)

    species = db.Column(db.Text,
                    nullable = False)

    photo_url = db.Column(db.Text,
                    nullable = True)
    
    age = db.Column(db.Integer,
                    nullable = True)

    notes = db.Column(db.Text,
                    nullable = True)
    
    available = db.Column(db.Boolean,
                    nullable = False,
                    default = True)
    

    #additional methods go here