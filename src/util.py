class UserInputError(Exception):
    pass


def validate_reference(title):
    """Validate a reference title, raising on invalid constraints."""
    if not isinstance(title, str):
        raise TypeError("Title must be a string")

    length = len(title)
    if length <= 1:
        raise UserInputError("Reference title length must be greater than 1")
    if length > 100:
        raise UserInputError("Reference title length must be less than 100")
