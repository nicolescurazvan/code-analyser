import errors


# Line parser
def ParseLine(line: str) -> dict[str, str | list[str]]:
    words = line.split()
    try:
        count = 0
        index = i = -1
        commands = ["TIME", "SIZE", "PLOT", "TABLE"]
        for word in words:
            i += 1
            if word in commands:
                count += 1
                index = i
        if count != 1:
            raise errors.UserError(errors.SyntaxMessage)
        elif index == 0 and words[index] in ["TIME", "SIZE"]:
            raise errors.UserError(errors.SyntaxMessage)
        elif index != 0 and words[index] in ["TABLE", "PLOT"]:
            raise errors.UserError(errors.SyntaxMessage)
        else:
            return {
                "label": " ".join(words[0:index]),
                "command": words[index],
                "args": words[index + 1 :],
            }
    except errors.UserError as e:
        print(e)
        return {"label": "", "command": "", "args": []}
