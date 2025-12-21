import analytics


def execute(line):
    words = line.split()
    function = words[0]
    command = words[1:]
    if function == "TIME":
        print(analytics.MeasureTime(command[1], command[2:]))
    elif function == "SIZE":
        print(analytics.FileSize(command[1]))
    else:
        print("WRONG")


def main():
    line = input()
    while line != "EXIT":
        execute(line)


if __name__ == "__main__":
    main()
