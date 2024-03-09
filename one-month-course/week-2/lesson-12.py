the_count = [1, 2, 3, 4, 5]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Evinha", 1/2, ["Oh no!", "A list inside a list"]]

# this for-loop goes through a list:
for number in the_count:
    print("this is count", number)

# same as above
for stock in stocks:
    print("Stock ticker", stock)

# we can go through mixed lists too
# I called it 'i' (shorts for item) since I don't know what's in it
for i in random_things:
    print("Here's a random thing:", i)
