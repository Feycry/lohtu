class UserInputError(Exception):
    pass

def validate_reference(title):

    if not isinstance(title, str):
        raise TypeError("Title must be a string")
    
    if len(title) <= 1:
        raise UserInputError("Reference title length must be greater than 1")

    if len(title) > 100:
          raise UserInputError("Reference title length must be less than 100")
