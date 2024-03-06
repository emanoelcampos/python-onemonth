# Reading the Python Code Step by Step

In this lesson, I went line by line through the Python code I just ran in the last lesson to understand what it does. I was introduced to Python syntax, how to store data in variables, and how to print information to the screen.

## Step by Stepe Explanation

Here's a step-by-step breakdown of the Python code from the last lesson:

### 1. Top of the file
```
import random
```

This imports other code. A library called `random` that later allows us to pick out a random bar or random person from our lists.

### 2. Lists of Bars & People

```
bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kendrick Lamar",
          "Samuel L. Jackson"]
```

These are lists of bars and people. They are going to be pulled into... 


### 3. Pick a random bar and a random person

```
random_bar = random.choice(bars)
random_person_one = random.choice(people)
```

This is where the script picks a random bar and a random person.

### 4. Print out the results

```
print(f"How about you go to {random_bar} with {random_person_one} 
```

This line prints out the random bar and random person. 
