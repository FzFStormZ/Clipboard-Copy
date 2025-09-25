import re

def has_special_chars(s: str) -> bool:
    """
    Export all the founded passwords inside a wordlist.

    :param s: String to check the condition.
    :type s: str
    :return: Has special characters or not.
    :rtype: bool

    """
    return bool(re.search(r"[^a-zA-Z0-9]", s))

def has_numbers(s: str) -> bool:
    """
    Export all the founded passwords inside a wordlist.

    :param s: String to check the condition.
    :type s: str
    :return: Has numbers or not.
    :rtype: bool

    """
    return bool(re.search(r"[0-9]", s))