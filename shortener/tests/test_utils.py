from shortener.utils import get_short_url


def test_getting_shortened_url():
    url = get_short_url()

    assert url.startswith("http://localhost:8000/shrt/")
    assert len(url) == 34
