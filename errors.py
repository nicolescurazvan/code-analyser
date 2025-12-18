ProgramMessage = """
      Code Analyser usage:\n
    1) main.py --cli\tfor CLI interaction
    2) main.py --file <file>\tfor using a script
"""

SyntaxMessage = """
    Correct Syntax:\n
    1) label TIME program args
    2) label SIZE file
    3) TABLE options
    4) PLOT options
    To exit shell: `EXIT`\n
"""


class UserError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class ProgramError(Exception):
    def __init__(self, program: str, args: str, err: str):
        msg = f"The test {program} {' '.join(args)} encountered an error:\n{err}"
        super().__init__(msg)


class SystemError(Exception):
    def __init__(self, err: str):
        super().__init__(err)
