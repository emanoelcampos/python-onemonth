# Dictionaries and Lists can be inside each other

# Lists inside dictionaries:
animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": []
}

# Dictionaries inside lists:
emanoel = {'name': 'emanoel', 'height': 70, 'shoe size': 8.5, 'hair': 'brown', 'eye': 'brown'}
david = {'name': 'david', 'height': 75, 'shoe size': 10, 'hair': 'brown', 'eye': 'blue'}
lucas = {'name': 'lucas', 'height': 68, 'shoe size': 9.5, 'hair': 'brown', 'eye': 'brown'}

people = [emanoel, david, lucas]
print(people)

for person in people:
    print(person)
