# Imports here
from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
#creates flask app wuth the secret key for debugging
app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"

#only for flask debug toolbar 
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#only for flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
db.create_all()

#routes here

@app.route('/')
def show_home_page():
    """displays home page for pet adoption agency"""

    pets = Pet.query.all()

    return render_template('home.html', pets = pets)

@app.route('/add-pet', methods=["GET", "POST"])
def add_pet():
    """add pet to homepage and handle form if POST request"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available = available)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/pets/<int:pet_id>', methods=["GET"])
def display_pet(pet_id):
    """displays information about the pet"""

    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_info.html', pet=pet)

@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def pet_edit(pet_id):
    """display and handle pet edit form"""

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        
        db.session.commit()

        return redirect(f'/pets/{pet_id}')

    else:

        return render_template('edit_pet_form.html', form=form, pet=pet)


