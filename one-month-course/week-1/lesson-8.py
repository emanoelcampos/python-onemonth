"""
Writing My Own Python Script

The concept of a randomizer script, and the next challenge!

The challenge

1. Write your own Python randomizer script.

2. Create your own version of the happy hour script. It can be ice cream or countries to visit or whatever.
"""

# Music Matching

import random

music = ["Kendrick Lamar",
         "Jorge Ben",
         "Luiz Melodia",
         "Hans Zimmer",
         "Criolo",
         "Pink Floyd"]

sport = ["basketball",
         "soccer",
         "cycling",
         "running",
         "tennis",
         "boxing"]

random_music = random.choice(music)
random_sport = random.choice(sport)

print(f"Today is perfect for listening to {random_music} while practicing {random_sport}.")
