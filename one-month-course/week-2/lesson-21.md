# Python Functions Strike Back

In this tutorial I learned how to write functions, arguments, and about scope.

## Function checklist
1. Function definitions begin with `def` 
2. A function name can only contain characters or an `_` (underscore)
3. Open parenthesis `(` right after function name 
4. Arguments are separated by commas 
5. Each argument must be unique (no duplicate names)
6. Close parenthesis and use colon `):`
7. Indent all lines of code in the function with a tab (required)
8. End function by de-indenting back to the same indent level as the def

## Too many or too few function arguments

When you add too many or too few arguments to a function:

```
print_two(first_name, 28, "Oops")
```

And try to run the file, you'll get an error:

```
$ python functions.py
Traceback (most recent call last):
  File "functions.py", line 16, in <module>
    print_two(first_name, 27, "Oops")
TypeError: print_two() takes 2 positional arguments but 3 were given
```

Now, you can change the argument order in a function. It's pretty common and convenient. 

```
print(concatenate(word_two='Emanoel', word_one='Campos'))
```

Everything that happens inside of a function is isolated from what happens outside a function. This is called **scoping**. 