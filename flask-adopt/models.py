from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

PHOTO_URL = 'https://cdn3.iconfinder.com/data/icons/avatars-9/145/Avatar_Cat-512.png'

class Pet(db.Model):
    """Adoptable pets"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text, 
                        nullable=True)
    url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image of generic pet or provided image"""
        return self.url or PHOTO_URL

def connect_db(app):

    db.app = app
    db.init_app(app)



