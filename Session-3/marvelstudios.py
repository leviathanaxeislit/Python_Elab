"""
"""
# Read the number of names
n = int(input())

# Read the character names
names = []
for i in range(n):
    names.append(input())

# Sort the names in alphabetical order
names.sort()

# Display the sorted names
for name in names:
    print(name)