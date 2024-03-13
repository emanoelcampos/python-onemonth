def uppercase_and_reverse(text):
    return reverse(text.upper())


def reverse(text):
    return text[::-1]


print(uppercase_and_reverse("This text is capitalized and reversed"))
