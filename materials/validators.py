from rest_framework.serializers import ValidationError


def validate_url(url):
    if not url.startswith("https://youtube.com"):
        raise ValidationError
