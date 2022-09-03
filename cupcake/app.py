"""Flask app for Cupcakes"""
# Imports here
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

#creates flask app wuth the secret key for debugging
app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"
CORS(app, resources={r"/api/*": {"origins": "*"}})

#only for flask debug toolbar 
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#only for flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

def serialize_cupcake(cupcake):
    """serializes data into JSON"""

    return {
        'id': cupcake.id,
        'flavor': cupcake.flavor,
        'size': cupcake.size,
        'rating': cupcake.rating,
        'image': cupcake.image
    }

#routes here
@app.route('/api/cupcakes', methods=['GET'])
def get_all_cupcakes():
    """returns data of all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    """returns data of single cupcake from cupcakes ID"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """creates a cupcake and updates the database"""

    data = request.json

    new_cupcake = Cupcake(
        flavor = data['flavor'],
        size = data['size'],
        rating = data['rating'],
        image = data['image'] or None
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """updates single cupcake in the database"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    data = request.json

    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data['image']

    db.session.commit()

    serialized = serialize_cupcake(cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Deletes cupcake from the database"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake_id)
    db.session.commit()

    return jsonify(message='Deleted')

@app.route('/')
def home_page():
    """returns home page view"""

    return render_template('home.html')
