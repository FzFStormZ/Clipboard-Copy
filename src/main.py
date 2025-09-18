from clipboard import xray

def main():
    # Starting the XRay :)  
    sniff = xray.XRay()

    # Collect a maximum of passwords...
    sniff.read_until_password() # Hello12@AdffrEZZ
    
    # Export all the passwords founded inside a wordlist
    with open("./wordlists/passwords.txt", "w") as wordlist:
        sniff.export_passwords(wordlist)

if __name__ == "__main__":
    main()