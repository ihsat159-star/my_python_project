# Take input from the user
text = input("Enter a sequence of numbers separated by spaces: ")

# Split input into a list of integers
items = [int(x) for x in text.split()]

# Sort items numerically (smallest to largest)
items.sort()

# Get length and middle index
n = len(items)
middle = n // 2

# Empty list for final result
result = []

# Add first half in reverse order
i = middle - 1
while i >= 0:
    result.append(items[i])
    i -= 1

# Add second half in normal order
i = middle
while i < n:
    result.append(items[i])
    i += 1

# Print result
for item in result:
    print(item, end=" ")
print()