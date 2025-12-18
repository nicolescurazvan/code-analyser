import sys

import analytics
import errors
import parser

# import stats

results = dict()


# CLI interface
def ProcessCLI():
    print("CLI mode activated")
    print(errors.SyntaxMessage)
    print()

    line = input()
    while line != "EXIT":
        obj = parser.ParseLine(line)
        print(obj["label"])
        if obj["command"] == "TIME":
            res = analytics.MeasureTime(obj["command"], obj["args"])
            results[obj["label"]] = res
        line = input()


# Script processing
def ProcessFile(file: str):
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
