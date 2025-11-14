from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    references = get_references()
    #unfinished = len([reference for reference in references if not reference.done])
    return render_template("index.html", references=references) 

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
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

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
