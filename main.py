import sys


class UserError(Exception):
    pass


def ProcessCLI():
    print("CLI mode activated")


def ProcessFile(file):
    try:
        f = open(file, "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print(f"There's no file named '{file}' here")


def main():
    try:
        if len(sys.argv) == 1:
            raise UserError
        if sys.argv[1] == "--cli" and len(sys.argv) == 2:
            ProcessCLI()
        elif sys.argv[1] == "--file" and len(sys.argv) == 3:
            ProcessFile(sys.argv[2])
        else:
            raise UserError
    except UserError:
        print("  Code Analyser usage:")
        print()
        print("1) main.py --cli\n\tfor CLI interaction")
        print("2) main.py --file <file>\n\tfor using a script")


if __name__ == "__main__":
    main()
