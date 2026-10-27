import secrets


def get_short_code() -> str:
    """
    Creates shortened url.

    :return: Shortened url
    """
    return secrets.token_urlsafe(5)
