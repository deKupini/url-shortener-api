from shortener.utils import get_short_code


def test_getting_short_code():
    code = get_short_code()

    assert isinstance(code, str)
    assert len(code) == 7
