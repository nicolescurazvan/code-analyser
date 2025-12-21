# code-analyser
---
A tool for analysing and benchmarking programs. It does the following tests:

* Measure and compare how much time different programs take to run. It works
by running the programs as subprocesses and counting the time.

* Measure and compare the size of the files.

The instructions are executed in a queue (first-in-first-out) structure. They
can be read from keyboard (via CLI) or from a file, one per line. After execution,
they are removed from the queue.

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
