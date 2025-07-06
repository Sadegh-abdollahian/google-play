from django.core.exceptions import ValidationError


def validate_icon_image_size(image):
    max_size_mb = 5
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image file too large ( > {max_size_mb}MB )")


def validate_max_age(value):
    if value > 18:
        raise ValidationError(f"Value cannot be greater than 999. You entered {value}.")


def validate_max_rate(value):
    if value > 5:
        raise ValidationError(f"Value cannot be greater than 5. You entered {value}.")
