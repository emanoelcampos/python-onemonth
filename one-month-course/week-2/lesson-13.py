# we can also build lists, first let's start with an empty one
people = []

people.append("Emanoel")
people.append("Ana")
people.append("David")
people.append("Lucas")

# now we can print them out too
print(people)

people.remove("Emanoel")
print(people)

for person in people:
    print("Person is:", person)
