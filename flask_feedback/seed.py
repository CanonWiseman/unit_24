from app import app
from models import db, User


db.drop_all()
db.create_all()

u1 = User(
    username = "Canon",
    password = "1234",
    email = "wisemancanon@gmail.com"
    first_name = "canon",
    last_name = "wiseman"
)

u2 = User(
    username = "Natalie",
    password = "12345",
    email = "NatRat@gmail.com"
    first_name = "Natalie",
    last_name = "Crutcher"
)

db.session.add_all([u1, u2])
db.session.commit()