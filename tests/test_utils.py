from src.utils import has_special_chars, has_numbers

def test_hash_special_chars():
    assert has_special_chars("hello!") is True      # exclamation mark
    assert has_special_chars("test@123") is True    # contains @
    assert has_special_chars("Café") is True        # accented character
    assert has_special_chars("abc#def") is True     # hash symbol
    assert has_special_chars("   ") is True         # spaces count as special chars

    assert has_special_chars("hello") is False
    assert has_special_chars("Test123") is False

def test_has_numbers():
    assert has_numbers("abc123") is True
    assert has_numbers("42") is True
    assert has_numbers("test0") is True
    assert has_numbers("no7yes") is True
    assert has_numbers("mix3dChars") is True

    assert has_numbers("hello") is False
    assert has_numbers("onlyTEXT") is False