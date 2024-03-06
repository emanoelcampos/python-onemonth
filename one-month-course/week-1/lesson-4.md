# How I ran my first Python Script

I ran my first Python script! In that lesson, I learned how to navigate the file system with the command line as well as how to run Python scripts. If I browsed GitHub for "Python scripts" I'd see that there were so many useful Python scripts (available for free!), but before I dove in too deep, I needed to start with the basics: my first Python script!

## Download the file 

I downloaded the file `happy_hour.py` provided in the lesson notes and moved the file to the `python` folder on my Desktop.

```
$ ls
happy_hour.py
```

## Run the file

To run the file, I typed:

`$ python happy_hour.py`

Those were the results!

```
$ python happy_hour.py
How about you go to The Dead Poet with tha tperson you forgot to text back?
$ python happy_hour.py
How about you go to The Hamilton with Samule L. Jackson?
$ python happy_hour.py
How about you go to Lion's Head Tavern with Samuel L. Jackson?
```


Note: I did not type the word `Python` because that would lead the command line to a different place. If I found that `$ python happy_hour.py` or `$ ls` returned error messages, I typed `exit` or hit `control+D`, which took me back to where I needed to be.

## Open the file

When I opened the file in IDE(I'm using PyCharm), it looked like this:

```
# What Should I Do Tonight?

import random

# Our list of bars
bars = ["Lion's Head Tavern",
        "The Hamilton",
        "1020 Bar",
        "Amsterdam Tavern",
        "The Heights",
        "The Dead Poet",
        "Prohibition"]

# Our list of friends
people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kendrick Lamar",
          "Samuel L. Jackson"]

random_bar = random.choice(bars)
random_person = random.choice(people)

print(f"How about you go to {random_bar} with {random_person}?")
```

Now, I went through happy_hour.py and read it out loud to myself. I got a sense of what's happening. I followed my gut instinct on what it says (didn't overthink it).