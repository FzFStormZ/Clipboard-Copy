import pyperclip as clip
from utils import utils
from pynput import keyboard

class XRay:
    def __init__(self, nb_caracs: int = 8, specials: bool = True, numbers: bool = True) -> None:
        self.passwords = set()
        self.conditions = {'nb_caracs': nb_caracs, 'specials': specials, 'numbers': numbers}
        self.keyboard = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def on_press(key) -> None:
        print("test")
        if key == keyboard.Key.enter:
            # Stop listener
            return False
        pass

    def on_release(key) -> None:
        print("test")
        pass

    # Check if the given text is actually a password according to the conditions of the instance
    def is_password(self, text: str) -> bool:
        nb = len(text) > self.conditions['nb_caracs']
        special = utils.has_special_chars(text)
        numbers = utils.has_numbers(text)
        return nb & special & numbers

    def read_current_data(self) -> None:
        text = clip.paste()
        if self.is_password(text):
            self.passwords.add(text)
            print(f"Password founded: {text}!")
            print(f"Added to the passwords list")
        else:
            print("Password not found :)")

    def read_until_password(self) -> None:
        # init variables
        text = ''
        password = ''

        # start the keyboard listener thread
        self.keyboard.start()

        while self.keyboard.is_alive():
            print("XRay activated... [CTRL+C] to stop the listening")
            text = clip.paste()
            if self.is_password(text) and password != text:
                password = text
                print(f"Password founded: {password}!")
                self.passwords.add(password)
                print(f"Added to the passwords list")
        print("Stopping the XRay...")
                
    # Put all the founded passwords inside a wordlist
    def export_passwords(self, file) -> None:
        pass