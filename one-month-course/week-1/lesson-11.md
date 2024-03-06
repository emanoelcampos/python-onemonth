# Debugging Python: To Error Is Human

No developer writes perfect code all the time. One thing I should expect is that my code won't always work as expected. In this lesson, I learned how to read error messages that are output to the terminal and identify the code that caused the error. Debugging is something I'll be using throughout the course, so by the time I complete it, I'll be quite adept at finding and fixing bugs in my code. In this lesson, I also learned how to get the most out of debugging with Google.

## Reading erros in Python

If a `)` parenthesis is forgotten when closing a line of code, the following error occurs:

*Command Line*

```
emanoel@ntbk-emanoel MINGW64 /d/python-one-month/one-month-course/week-1 (master)
$ python lesson-10.py
  File "D:\python-one-month\one-month-course\week-1\lesson-10.py", line 9
    print("Pois a tamba está tocando"
         ^
SyntaxError: '(' was never closed
```

Sometimes error messages are clear, and sometimes they are not. This error message is scary, but let's take a look.

The first line tells the file name and the line it thinks the error is on:

*Command Line*

```
emanoel@ntbk-emanoel MINGW64 /d/python-one-month/one-month-course/week-1 (master)
$ python lesson-10.py
  File "D:\python-one-month\one-month-course\week-1\lesson-10.py", line 9
```

The next line is the code in the file from this script and the ^ shows you where it thinks the error is. And the final line is the actual error message (you can use this to look up more information).

## How to troubleshoot using Google

Whenever you get stuck, Google your error and see if you can find the solution.

