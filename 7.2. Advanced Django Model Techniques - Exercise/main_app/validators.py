from django.core.exceptions import ValidationError


def validate_name(value):
    for symbol in value:
        if not (symbol.isalpha() or symbol.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


def check_age(value):
    if value < 18:
        raise ValidationError("Age must be greater than 18")