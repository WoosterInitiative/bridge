import pytest


@pytest.fixture
def django_settings():
    return {
        "ALLOWED_HOSTS": ["localhost"],
        "DATABASES": {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "db.sqlite3",
            }
        },
        "STATIC_URL": "/static/",
        "BASE_DIR": "test",
        "DEBUG": True,
        "SECRET_KEY": "secret",
    }
