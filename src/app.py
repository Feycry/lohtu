from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db, delete_reference
from repositories.reference_repository import get_references, create_reference, get_reference_type_required_fields, get_reference, update_reference
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
    reference_type = request.args.get("reference_type", "")
    
    # Get required fields for this reference type
    required_fields = []
    if reference_type:
        required_fields = get_reference_type_required_fields(reference_type)
    
    # All possible fields in the form
    all_fields = [
        'author', 'title', 'journal', 'booktitle', 'year', 'publisher', 
        'school', 'institution', 'url', 'doi', 'editor', 'volume', 
        'number', 'series', 'pages', 'address', 'month', 'organization',
        'edition', 'howpublished', 'note', 'type'
    ]
    
    # Separate required and optional fields
    optional_fields = [field for field in all_fields if field not in required_fields]
    
    return render_template("new_reference.html", 
                         reference_type=reference_type,
                         required_fields=required_fields,
                         optional_fields=optional_fields)

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    """Creates a new reference with the provided form data."""
    # Get reference type
    reference_type = request.form.get("reference_type")
    
    # Get all possible fields
    author = request.form.get("author")
    title = request.form.get("title")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")
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
    edition = request.form.get("edition")
    howpublished = request.form.get("howpublished")
    institution = request.form.get("institution")
    journal = request.form.get("journal")
    note = request.form.get("note")
    school = request.form.get("school")
    type_field = request.form.get("type")

    try:
        validate_reference(title)
        create_reference(
            reference_type=reference_type,
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
            publisher=publisher,
            edition=edition,
            howpublished=howpublished,
            institution=institution,
            journal=journal,
            note=note,
            school=school,
            type=type_field
        )
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

@app.route("/edit_reference")
def edit():
    """Renders the form for editing an existing reference."""
    reference_id = request.args.get("reference_id")
    
    if not reference_id:
        flash("Reference ID is required for editing.")
        return redirect("/")
    
    reference = get_reference(reference_id)
    
    if not reference:
        flash("Reference not found.")
        return redirect("/")
    
    # Get required fields for this reference type
    required_fields = get_reference_type_required_fields(reference.ref_type)
    
    # All possible fields in the form
    all_fields = [
        'author', 'title', 'journal', 'booktitle', 'year', 'publisher', 
        'school', 'institution', 'url', 'doi', 'editor', 'volume', 
        'number', 'series', 'pages', 'address', 'month', 'organization',
        'edition', 'howpublished', 'note', 'type'
    ]
    
    # Separate required and optional fields
    optional_fields = [field for field in all_fields if field not in required_fields]
    
    return render_template("edit_reference.html",
                         reference=reference,
                         required_fields=required_fields,
                         optional_fields=optional_fields)

@app.route("/update_reference", methods=["POST"])
def edit_reference():
    """Updates an existing reference with the provided form data."""
    reference_id = request.form.get("reference_id")
    
    if not reference_id:
        flash("Reference ID is required for editing.")
        return redirect("/")
    
    # Get reference type (not editable, so get from existing reference)
    reference = get_reference(reference_id)
    if not reference:
        flash("Reference not found.")
        return redirect("/")
    
    reference_type = reference.ref_type
    
    # Get all possible fields
    author = request.form.get("author")
    title = request.form.get("title")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")
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
    edition = request.form.get("edition")
    howpublished = request.form.get("howpublished")
    institution = request.form.get("institution")
    journal = request.form.get("journal")
    note = request.form.get("note")
    school = request.form.get("school")
    type_field = request.form.get("type")

    try:
        validate_reference(title)
        update_reference(
            reference_id=reference_id,
            reference_type=reference_type,
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
            publisher=publisher,
            edition=edition,
            howpublished=howpublished,
            institution=institution,
            journal=journal,
            note=note,
            school=school,
            type=type_field
        )
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect(f"/edit_reference?reference_id={reference_id}")

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
