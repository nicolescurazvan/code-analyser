import subprocess
from pathlib import Path
from time import perf_counter

def get_cmd(name):
    if name.find(".py") != None:
        return ["python3", name]
    else:
        return ["./" + name]

def checker(exec, finput, fref):
    fin = open(Path(finput), "r")
    fout = open(Path("out.txt"), "w")
    ref = open(Path(fref), "r")

    process = subprocess.Popen(get_cmd(exec), stdin = fin, stdout = fout,
                               stderr = subprocess.PIPE)
    process.wait()
    print(process.stderr)
    print(get_cmd(exec))

def measure(exec, finput):
    fin = open(Path(finput), "r")
    fout = open(Path("out.txt"), "w")
    beg = perf_counter()
    process = subprocess.Popen(get_cmd(exec), stdin = fin, stdout = fout,
                           stderr = subprocess.DEVNULL)
    process.wait()
    end = perf_counter()
    return end - beg

checker("dummy.py", "input.txt", "ref.txt")
print(measure("dummy.py", "input.txt"))