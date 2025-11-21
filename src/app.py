from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db, delete_reference
from repositories.reference_repository import get_references, create_reference
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    """Renders the main page with the list of references."""
    references = get_references()
    #unfinished = len([reference for reference in references if not reference.done])
    return render_template("index.html", references=references) 

@app.route("/new_reference")
def new():
    """Renders the form for creating a new reference."""
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    """Creates a new reference with the provided form data."""
    # Required fields
    author = request.form.get("author")
    title = request.form.get("title")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")
    
    # Optional fields
    url = request.form.get("url")
    doi = request.form.get("doi")
    editor = request.form.get("editor")
    volume = request.form.get("volume")
    number = request.form.get("number")
    series = request.form.get("series")
    pages = request.form.get("pages")
    address = request.form.get("address")
    month = request.form.get("month")
    organization = request.form.get("organization")
    publisher = request.form.get("publisher")

    try:
        validate_reference(title)
        create_reference(
            author=author,
            title=title,
            booktitle=booktitle,
            year=year,
            url=url,
            doi=doi,
            editor=editor,
            volume=volume,
            number=number,
            series=series,
            pages=pages,
            address=address,
            month=month,
            organization=organization,
            publisher=publisher
        )
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

@app.route("/edit")
def edit():
    return render_template("edit_reference.html")

@app.route("/edit_reference", methods=["POST"])
def edit_reference():
    pass

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        """Resets the database by clearing all references."""
        reset_db()
        return jsonify({ 'message': "db reset" })

@app.route("/delete_ref", methods=["POST"])
def del_reference():
    """Deletes a reference by its ID."""
    reference_id = request.form.get("reference_id")
    if not reference_id:
        flash("Reference ID is required for deletion.")
    elif delete_reference(reference_id):
        return redirect("/")
    else:
        flash("Deletetion failed.")
    return redirect("/")
