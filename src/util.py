class UserInputError(Exception):
    pass


def validate_reference(title):
    """Validate a reference title, raising on invalid constraints."""
    if not isinstance(title, str):
        raise TypeError("Title must be a string")
    if title.isspace():
        raise UserInputError("Title cannot be empty or whitespace only")

    length = len(title)
    if length <= 1:
        raise UserInputError("Reference title length must be greater than 1")
    if length > 100:
        raise UserInputError("Reference title length must be less than 100")


def validate_required_fields(reference_type, fields):
    """Validate presence of required fields for given reference type.
    Expects fields as a dict of field -> value. Raises UserInputError with a
    specific message when a required field is missing or empty.
    """
    required_map = {
        "article": ["author", "title", "journal", "year"],
        "book": ["author", "title", "publisher", "year"],
        "booklet": ["title"],
        "conference": ["author", "title", "booktitle", "year"],
        "inbook": ["author", "title", "booktitle", "publisher", "year"],
        "incollection": ["author", "title", "booktitle", "publisher", "year"],
        "inproceedings": ["author", "title", "booktitle", "year"],
        "manual": ["title"],
        "mastersthesis": ["author", "title", "school", "year"],
        "misc": [],
        "phdthesis": ["author", "title", "school", "year"],
        "proceedings": ["title", "year"],
        "techreport": ["author", "title", "institution", "year"],
        "unpublished": ["author", "title"],
    }

    reqs = required_map.get(reference_type, [])
    for key in reqs:
        val = fields.get(key)
        if val is None or (isinstance(val, str) and val.strip() == ""):
            raise UserInputError(f"{key.capitalize()} is required for @{reference_type}")
