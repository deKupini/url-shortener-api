from rest_framework import status
from rest_framework.test import APIClient

from ..models import URLMapping


SHRT_URL = "/shrt/"


def test_create_short_url(db, client: APIClient):
    test_url = "https://www.google.com"

    response = client.post(SHRT_URL, {"original_url": test_url})

    assert response.status_code == status.HTTP_201_CREATED
    assert "short_url" in response.data
    assert len(response.data.get("code")) == 7


def test_create_short_url_for_mapped_url(db, client:APIClient):
    test_url = "https://www.google.com"
    test_code = "1234567"
    URLMapping.objects.create(original_url=test_url, code=test_code)

    response = client.post(SHRT_URL, {"original_url": test_url})

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "original_url": test_url,
        "code": test_code,
        "short_url": f"http://testserver{SHRT_URL}{test_code}/"
    }
    assert URLMapping.objects.count() == 1


def test_create_short_url_for_invalid_url(db, client: APIClient):
    test_url = "invalid_url"

    response = client.post(SHRT_URL, {"original_url": test_url})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert not URLMapping.objects.count()


def test_get_original_url(db, client: APIClient):
    test_url = "https://www.google.com"
    test_code = "1234567"

    URLMapping.objects.create(original_url=test_url, code=test_code)

    response = client.get(f"{SHRT_URL}{test_code}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("original_url") == test_url


def test_get_not_existing_url(db, client: APIClient):
    test_code = "1234567"

    response = client.get(f"{SHRT_URL}{test_code}/")

    assert response.status_code == status.HTTP_404_NOT_FOUND
