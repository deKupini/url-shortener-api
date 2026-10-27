import secrets


def get_short_url() -> str:
    """
    Creates shortened url.

    :return: Shortened url
    """
    token = secrets.token_urlsafe(5)
    return f"http://localhost:8000/shrt/{token}"
