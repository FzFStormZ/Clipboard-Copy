from clipboard import xray

def main():
    print("Checking if there is a current password inside the clipboard...")
    test = xray.XRay()
    test.read_current_data()
    # Run the checking
    # If found, print it
    # Else
    print("XRay activated... Be careful to not put your password inside the clipboard :)")
    # while 
    # Print if a new password is detected !
    # Create at the end of the program a list of all the passwords founded and put it inside a wordlist 




if __name__ == "__main__":
    main()