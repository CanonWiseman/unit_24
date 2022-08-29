from models import Pet, db
from app import app

#Create tables

db.drop_all()
db.create_all()


#empty tables

Pet.query.delete()


# Add Pets

Behr = Pet(name = 'Behr', species = 'Dog', photo_url = 'https://m.media-amazon.com/images/I/61BOxbSnFuL._AC_SX466_.jpg', age = 8, notes = 'Spry, youthful, easy around families')
Spartacus = Pet(name = 'Spartacus', species = 'Dog', photo_url = 'https://static.boredpanda.com/blog/wp-content/uploads/2016/09/rescued-smiling-pitbull-meaty-4.jpg', age = 6, notes = 'Good dog for a single, active person. Good around other dogs')
Saki = Pet(name = 'Saki', species = 'Cat', photo_url = 'https://i.pinimg.com/originals/b0/04/30/b00430fba960aa03ef155bfd2005da9e.jpg', age = 2, notes = 'Very sweet, loving and loyal, needs a permanent home(PLEASE!)')

db.session.add_all([Behr, Spartacus, Saki])
db.session.commit()