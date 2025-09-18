from clipboard import xray

def main():
    print("Checking if there is a current password inside the clipboard...")
    # start the keyboard listener thread    
    test = xray.XRay()
    test.read_until_password() # Hello12@AdffrEZZ
    
    # Create at the end of the program a list of all the passwords founded and put it inside a wordlist 

if __name__ == "__main__":
    main()