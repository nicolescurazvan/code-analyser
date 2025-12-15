import sys

import analytics
import errors
import instruction


# CLI interface
def ProcessCLI():
    print("CLI mode activated")


# Script processing
def ProcessFile(file):
    try:
        f = open(file, "r")
        print(f.read())
        f.close()

    except FileNotFoundError:
        print(f"File '{file}' doesn't exist")


# Main function
def main():
    try:
        if len(sys.argv) == 1:
            raise errors.UserError
        if sys.argv[1] == "--cli" and len(sys.argv) == 2:
            ProcessCLI()
        elif sys.argv[1] == "--file" and len(sys.argv) == 3:
            ProcessFile(sys.argv[2])
        else:
            raise errors.UserError
    except errors.UserError as e:
        print(e)


if __name__ == "__main__":
    main()
