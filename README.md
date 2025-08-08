# code-analyser

A python script to check and analyse code easily. It performs two kinds of tests:
1) __Checker:__ checks whether the program is correct and tells where the error is.
2) __Measure:__ measures how fast the program is.

__Checker__ works by running the following command: `[program] [args] < [input] > [output] 2>> [log]`
and checking for errors and, if there are no errors, to see if the output is correct using a
reference file.

__Measure__ works by running the program and measuring the time it takes to complete. The results
are shown in a plot.

## Technologies used:
* Python
* TkInter
