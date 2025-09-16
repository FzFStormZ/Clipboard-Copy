import re

def has_special_chars(s: str) -> bool:
    return bool(re.search(r"[^a-zA-Z0-9]", s))

def has_numbers(s: str) -> bool:
    return bool(re.search(r"[0-9]", s))