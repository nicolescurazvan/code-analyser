import subprocess
from pathlib import Path
from time import perf_counter_ns

import errors


# Measure running time
def MeasureTime(program, args):
    try:
        command = [Path(program)] + args
        beg = perf_counter_ns()
        result = subprocess.run(command, capture_output=False)
        end = perf_counter_ns()
        return end - beg
    except subprocess.SubprocessError as e:
        print(f"Error! ({program}  {' '.join(args)})\n{e}")


# Execute a command
def Execute(command):
    try:
        result = subprocess.run(command)
        return result.stdout
    except subprocess.SubprocessError:
        print(f"Error! ({' '.join(command)})\n{e}")


# Size of a file
def FileSize(file: str) -> int:
    try:
        size = Path(file).stat().st_size
        return size
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
