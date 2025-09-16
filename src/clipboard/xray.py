import pyperclip as clip
from utils import utils

class XRay:
    def __init__(self, nb_caracs: int = 8, specials: bool = True, numbers: bool = True) -> None:
        self.passwords = []
        self.conditions = {'nb_caracs': nb_caracs, 'specials': specials, 'numbers': numbers}

    def is_password(self, text: str) -> bool:
        nb = len(text) > self.conditions['nb_caracs']
        special = utils.has_special_chars(text)
        numbers = utils.has_numbers(text)
        return nb & special & numbers

    def read_current_data(self) -> None:
        text = clip.paste()
        if self.is_password(text):
            self.passwords.append(text)
            print(f"Password founded: {text}")
        else:
            print("Password not found :)")

    def read_until_password(self) -> None:
        clip.paste
        pass

    def export_passwords(self, file) -> None:
        pass