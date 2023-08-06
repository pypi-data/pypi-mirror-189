from src.woomodule.app.app import get_str


def test_get_str_positive():
    assert type(get_str()) == str
