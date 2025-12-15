class UserError(Exception):
    def __init__(self):
        self.message = """  Code Analyser usage:\n
        1) main.py --cli\n\tfor CLI interaction\n
        2) main.py --file <file>\n\tfor using a script\n
        """
        super().__init__(self.message)


class ProgramError(Exception):
    def __init__(self, program, args, err):
        msg = f"The test {program} {' '.join(args)} encountered an error:\n{err}"
        super().__init__(msg)


class SystemError(Exception):
    def __init__(self, err):
        super().__init__(err)
