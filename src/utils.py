def validate_numbers(a, b):
    if (
        isinstance(a, bool)
        or isinstance(b, bool)
        or not isinstance(a, (int, float))
        or not isinstance(b, (int, float))
    ):
        raise TypeError("Both inputs must be numbers.")


def add(a, b):
    validate_numbers(a, b)
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    return a * b
