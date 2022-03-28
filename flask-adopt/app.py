from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "whaleshark21"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
db.create_all()

@app.route("/")
def homepage():

    """Show homepage w/pets"""
    pets = Pet.query.all()
    return render_template('pet_index.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        url = form.url.data
        notes = form.notes.data

        new_pet = Pet(name =name, species=species, url=url, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {new_pet.name}")

        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show pet edit form and handle edit."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.url = form.url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"Pet {pet.name} updated!")
        return redirect("/")

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)

