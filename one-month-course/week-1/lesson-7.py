import random

bars = ["Lion's Head Tavern",
        "The Hamilton",
        "1020 Bar",
        "Amsterdam Tavern",
        "The Heights",
        "The Dead Poet",
        "Prohibition"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kendrick Lamar",
          "Samuel L. Jackson",
          "Jorge Ben"]

random_bar = random.choice(bars)
random_person_one = random.choice(people)
random_person_two = random.choice(people)

print(f"How about you go to {random_bar} with {random_person_one} and {random_person_two}?")
