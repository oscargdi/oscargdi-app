from django.conf import settings
from django.http import HttpRequest


def heroku_context(request: HttpRequest):
    """Add Heroku metadata to the context."""
    return {
        "app_name": settings.HEROKU_METADATA["APP_NAME"],
        "release_version": settings.HEROKU_METADATA["RELEASE_VERSION"],
        "release_created_at": settings.HEROKU_METADATA["RELEASE_CREATED_AT"],
        "slug_commit": settings.HEROKU_METADATA["SLUG_COMMIT"],
        "slug_description": settings.HEROKU_METADATA["SLUG_DESCRIPTION"],
    }
