# code-analyser
---
A tool for analysing and benchmarking programs. It does the following tests:

* Measure and compare how much time different programs take to run. It works
by running the programs as subprocesses and counting the time. It's also
simple to use:

1) You add programs to the test:
> `ADD program [arguments]`

2) You run the test:
> `RUN`
