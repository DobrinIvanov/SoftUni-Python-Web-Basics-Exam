from django.core.exceptions import ValidationError


def Between1980_2049Validator(value):
    if value > 2049 or value < 1980:
        raise ValidationError('Year must be between 1980 and 2049')
