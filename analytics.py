import subprocess
from pathlib import Path
from time import perf_counter_ns


# Measure running time
def MeasureTime(program: str, args: list[str]) -> str:
    try:
        command = [Path(program)] + args
        beg = perf_counter_ns()
        result = subprocess.run(command)
        end = perf_counter_ns()
        print(result.stdout)
        t = end - beg
        if t < 1000:
            return f"{t}ns"
        elif t < 1e6:
            return f"{t / 1000:.2f}us"
        elif t < 1e9:
            return f"{t / 1e6:.2f}ms"
        else:
            return f"{t / 1e9:.2f}s"
    except subprocess.SubprocessError as e:
        print(f"Error! ({program}  {' '.join(args)})\n{e}")


# Size of a file
def FileSize(file: str) -> str:
    try:
        s = Path(file).stat().st_size
        if s < (1 << 10):
            return f"{s}B"
        elif s < (1 << 20):
            return f"{s / (1 << 10):.1f}KB"
        elif s < (1 << 30):
            return f"{s / (1 << 20):.1f}MB"
        elif s < (1 << 40):
            return f"{s / (1 << 30):.1f}GB"
        else:
            return f"{s / (1 << 40):.1f}TB"
    except FileNotFoundError as e:
        print(e)
        return ""
    except PermissionError as e:
        print(e)
        return ""
