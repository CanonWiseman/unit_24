# Imports here
from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from flask_bcrypt import Bcrypt
from forms import AddUserForm

#creates flask app wuth the secret key for debugging
app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"


#only for flask debug toolbar 
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#only for flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()
bcrypt = Bcrypt()

#routes here
@app.route('/')
def root_page():
    """redirects user to login page"""

    return redirect('/register')

@app.route('/register', methods=['GET','POST'])
def register():
    """displays and processes form for user registration"""

    form = AddUserForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)

        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id 
        return redirect('/secret')

    else:

        return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login:
    """displays users login form and athenticates user"""

    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.authenticate(name, pwd)

        if user:
            session["user_id"] = user.id
            return redirect('/secret')

        else:
            form.username.errors = ["Invalid username or password, please try again"]

    else:
        return render_template('login.html', form=form)

@app.route('/secret', methods=["GET"])
def secret():
    

        
