from django.utils.crypto import get_random_string

from core.models import ShortenedURL


def get_short_id():
    while True:
        id = get_random_string(length=8)
        if not ShortenedURL.objects.filter(id=id).exists():
            return id
