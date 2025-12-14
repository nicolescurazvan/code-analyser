# code-analyser
---
A tool for analysing and benchmarking programs. It does the following tests:

* Measure and compare how much time different programs take to run. It works
by running the programs as subprocesses and counting the time.

* Execute programs without analysing them.

* Measure and compare the size of the files.

The instructions are executed in a queue (first-in-first-out) structure. They
can be read from keyboard (via CLI) or from a file, one per line. After execution,
they are removed from the queue. The `RUN` command empties the queue.

---
## Program usage:

* CLI mode: `main.py --cli`
* From a script: `main.py --file [file name]`

---
## Why use this script?

It's a complex, yet very simple tool that can benchmark programs, check
algorithmic efficiency and it's programmable via scripts and the CLI shell
(similar to Python IDLE shell or bash/zsh terminal shells from the Unix
systems). It can display and save the output in many ways.

This can help programmers make more efficient code by teaching them how good
their algorithms actually are as time and especially memory efficiency are 
essential for developing high-quality software or APIs

Why Python? Because it's a simple, yet versatile programming language that
makes combining different technologies simpler than languages like C/C++ and
works flawlessly on all platforms with a Python interpreter.

---
## Syntax:

* Measure the execution time of a program:
`TIME <program> [args]`
where `program` is the name of the executable and its arguments are `args`. 
(for interpreted languages, the interpreting program must be explicitly given,
e.g. python3 for Python)

* Execute a command or a program:
`EXECUTE <command>` to execute `command`

* Measure the size of a file:
`SIZE <file>` where file is the path to the file

* Run the commands in the queue:
`RUN [FORMAT options]`, where `options` are the options and `FORMAT` is 
the format of the representation of results.

**Available Formats:**
