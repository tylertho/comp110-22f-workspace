"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls
i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total score: {sum}")

# rolls: list[int] = list()
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access and individual item
# print(rolls[0])
# print(rolls[1])

# # Access the length of a list
# print(len(rolls))

# # Access the last item of a list
# print(rolls[len(rolls)-1])