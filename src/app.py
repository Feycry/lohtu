from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference, set_done
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    references = get_references()
    unfinished = len([reference for reference in references if not reference.done])
    return render_template("index.html", references=references, unfinished=unfinished) 

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    content = request.form.get("content")

    try:
        validate_reference(content)
        create_reference(content)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

@app.route("/toggle_reference/<reference_id>", methods=["POST"])
def toggle_reference(reference_id):
    set_done(reference_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
