def validate_string(value: str)-> str:
    if isinstance(value, str):
        return value
    else:
        raise TypeError("The value must be a string.")

def validate_int(value: int)-> int:
    if isinstance(value, int):
        return value
    else:
        raise TypeError("The value must be a number.")