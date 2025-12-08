import re
from urllib.parse import urlencode
from flask import redirect, render_template, request, jsonify, flash, Response
import requests
from db_helper import reset_db, delete_reference, setup_db, tables
from repositories.reference_repository import get_references, create_reference, get_reference_type_required_fields, get_reference, update_reference
from config import app, test_env
from util import validate_reference, UserInputError
from entities.all_fields import COLUMN_KEYS


@app.route("/")
def index():
    """Renders the main page with the list of references."""
    # Read optional search query from GET params and pass it to repository
    q = request.args.get("q", "").strip()
    references = get_references(q if q else None)

    return render_template("index.html", references=references, q=q, title="Reference app")

@app.route("/new_reference")
def new():
    """Renders the form for creating a new reference."""
    reference_type = request.args.get("reference_type", "")


    required_fields = []
    if reference_type:
        required_fields = get_reference_type_required_fields(reference_type)


    optional_fields = [field for field in COLUMN_KEYS if field not in required_fields]

    # Get prefilled data from session or query params (from DOI lookup)
    prefill = {field: request.args.get(field, "") for field in COLUMN_KEYS}

    return render_template("new_reference.html",
                         reference_type=reference_type,
                         required_fields=required_fields,
                         optional_fields=optional_fields,
                         prefill=prefill)

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    """Creates a new reference with the provided form data."""

    reference_type = request.form.get("reference_type")


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
    except (UserInputError, TypeError) as error:
        flash(str(error))

        return redirect(f"/new_reference?reference_type={reference_type}")

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



    ref_type = getattr(reference, "ref_type", None)
    required_fields = get_reference_type_required_fields(ref_type) if ref_type else []


    all_fields = [
        'author', 'title', 'journal', 'booktitle', 'year', 'publisher', 
        'school', 'institution', 'url', 'doi', 'editor', 'volume', 
        'number', 'series', 'pages', 'address', 'month', 'organization',
        'edition', 'howpublished', 'note', 'type'
    ]


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


    reference = get_reference(reference_id)
    if not reference:
        flash("Reference not found.")
        return redirect("/")

    reference_type = getattr(reference, "ref_type", None)


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
    except (UserInputError, TypeError) as error:
        flash(str(error))
        return redirect(f"/edit_reference?reference_id={reference_id}")

@app.route("/export")
def export():
    """Starts a download for all references in a single .bib file"""
    references = get_references()

    # Build content in BibTeX format
    content = ""
    for ref in references:
        content += ref.to_bibtex()
        content += "\n\n"

    # Create a response with the content as a downloadable bib file
    return Response(
        content,
        mimetype="text/plain",
        headers={
            "Content-Disposition": "attachment; filename=references.bib"
        }
    )

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        """Resets the database by clearing all references."""
        # Ensure schema exists in CI containers
        existing = tables()
        if not existing or "reftype" not in existing or "refs" not in existing:
            setup_db()
        else:
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

@app.route("/lookup_doi", methods=["POST"])
def lookup_doi():
    """Looks up a DOI and redirects to new_reference with parsed BibTeX fields."""
    doi = request.form.get("doi", "").strip()

    if not doi:
        flash("DOI is required")
        return redirect("/new_reference")

    # Fetch BibTeX from DOI
    base_url = "https://doi.org/"
    url = base_url + doi
    headers = {"Accept": "application/x-bibtex"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        bibtex = response.text

        # Parse BibTeX entry
        fields = {}

        # Extract reference type
        type_match = re.search(r'@(\w+)\{', bibtex)
        if type_match:
            fields['reference_type'] = type_match.group(1).lower()

        # Extract fields using regex - handle both {} and "" delimiters
        # This regex handles multi-line values and nested braces better
        field_pattern = re.compile(r'(\w+)\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}|(\w+)\s*=\s*"([^"]*)"')
        for match in field_pattern.finditer(bibtex):
            if match.group(1):  # Brace-delimited
                field_name = match.group(1).lower()
                field_value = match.group(2).strip()
            else:  # Quote-delimited
                field_name = match.group(3).lower()
                field_value = match.group(4).strip()
            fields[field_name] = field_value

        # Build redirect URL with query parameters
        params = urlencode(fields)
        flash("DOI lookup successful! Fields have been populated.")
        return redirect(f"/new_reference?{params}")

    except requests.exceptions.RequestException as e:
        flash(f"Error resolving DOI: {str(e)}")
        return redirect("/new_reference")
