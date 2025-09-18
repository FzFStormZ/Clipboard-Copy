import pyperclip as clip
from utils import utils
import time
from sshkeyboard import listen_keyboard, stop_listening
import threading

class XRay:
    def __init__(self, nb_caracs: int = 8, specials: bool = True, numbers: bool = True) -> None:
        self.passwords = set()
        self.conditions = {'nb_caracs': nb_caracs, 'specials': specials, 'numbers': numbers}
        self.exit = False
        
        clip.set_clipboard('xclip')

        # Thread for the keyboard monitoring
        thread = threading.Thread(target=listen_keyboard, kwargs={"on_press": self.press, "until": None}, daemon=True)
        thread.start()

    def press(self, key):
        if key == "esc":
            self.exit = True
            stop_listening() # to avoid block the keyboard inside the current terminal

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
            print(f"Potential password founded: {text}!")
            print(f"Added to the passwords list")
        else:
            print("Password not found :)")

    def read_until_password(self) -> None:
        # init variables
        text = ''
        password = ''

        while not self.exit:
            print("XRay activated... [ESC] to stop the listening")
            text = clip.paste()
            if self.is_password(text) and password != text:
                password = text
                print(f"Potential password founded: {password}!")
                self.passwords.add(password)
                print(f"Added to the passwords list")
            
            time.sleep(1)
        print("Stopping the XRay...")
                
    # Put all the founded passwords inside a wordlist
    def export_passwords(self, file) -> None:
        pass