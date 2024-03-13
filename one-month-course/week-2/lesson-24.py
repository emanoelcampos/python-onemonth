# This method breaks up text into words for us
def break_words(text):
    return text.split()


# Counts the number of words
def count_words(words):
    return len(words)


# Sorts the words (alphabetically)
def sort_words(words):
    return sorted(words)


# Takes in a full sentence and returns the sorted words
def sort_sentence(sentence):
    break_sentence = break_words(sentence)
    return sort_words(break_sentence)


# Prints the first word after popping it off
def print_first_word(words):
    print(words.pop(0))


# Prints the last word after popping it off
def print_last_word(words):
    print(words.pop())


# Prints the first and last words of the sentence
def print_first_and_last_word(sentence):
    print_first_word(break_words(sentence))
    print_last_word(break_words(sentence))


demitri_martin_joke = """"I used to play sports. 
Then I realized you can buy trophies. Now I am good at everything."""

print("----------")
print(demitri_martin_joke)
print("----------")

bottles_of_beer = 100 + 10 - 15 + 4
print("This should be ninety-nine:", bottles_of_beer)


def sing(bottles):
    for number in reversed(range(bottles + 1)):
        if number > 0:
            print_verse(number)
        else:
            print_last_verse()


def print_verse(bottles):
    print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer")
    print("Take one down and pass it around,", bottles - 1, "bottles of beer on the wall.\n")


def print_last_verse():
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")


sing(bottles_of_beer)

sentence = """I think it's interesting that 'cologne' rhymes with 'alone'"""

words = break_words(sentence)
sorted_words = sort_sentence(sentence)

print(f"{sentence} has {count_words(words)} words")
print("The words are:", words)
print("The sorted words are:", sorted_words)

print_first_word(words)
print_last_word(words)
print_first_and_last_word(sentence)
