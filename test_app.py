from app import get_greeting

def test_get_greeting():
    assert get_greeting() == "Hello, CI/CD World!"
