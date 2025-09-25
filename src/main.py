import xray
import argparse

def main():
    """
    Main function of our program.

    """
    # Starting the XRay :)
    args = parser.parse_args()
    print(args)
    sniff = xray.XRay(args.verbose, int(args.length), args.no_specials, args.no_numbers)

    # Collect a maximum of passwords...
    sniff.read_until_password()
    
    # Export all the passwords founded inside a wordlist
    with open("src/wordlists/" + args.wordlist, "w") as wordlist:
        sniff.export_passwords(wordlist)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Clipboard XRay',
        usage='main.py [options]',
        description='Monitor the clipboard in real time and analyze its content to detect the possible presence of passwords')

    parser.add_argument('-w', '--wordlist', action='store', help='file to store the passwords (default: %(default)s)', default='passwords.txt')
    parser.add_argument('-v', '--verbose', action='store_true')

    conditions = parser.add_argument_group('password conditions')
    conditions.add_argument('-l', '--length', action='store', help='minimum number of caracters for a password (default: %(default)s)', default=8)
    conditions.add_argument('--no-specials', action='store_true')
    conditions.add_argument('--no-numbers', action='store_true')

    main()