# More Debugging in Python

### Debugging is an essential skill in a developer's toolkit. 

When creating files in Python, it is important to avoid naming conflicts with standard modules or internal libraries, such as `math.py`. This can cause errors as the Python interpreter may try to import your custom file instead of the corresponding standard module.
```
$ python happy_hour.py
Let's do some math!
('What is the answer to life, the universe, and everything?', 42)
Is it true that 5 * 2 > 3 * 4?
False
('What is 5 * 2?', 10)
('What is 3 * 4?', 12)
Traceback (most recent call last):
  File "happy_hour.py", line 3, in <module>
    import random
  File "/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py", line 45, in <module>
    from math import log as _log, exp as _exp, pi as _pi, e as _e, ceil as _ceil
ImportError: cannot import name log
```

A quick Google search for the error message (ImportError: cannot import name log:

*Is it possible that you have a file named `math.py` in the same directory as the program you are running? If so python tries to import it before the math module.* 

**Solution: Just rename it to something else.**