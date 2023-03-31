"""Question description
In our institution celebrates the independence day. Our NCC team forms a group to perform the march past in the sports ground. Can you help the NCC leader to make the pattern to perform the march past in a particular formation.
Constraints
Input Format:
First line represent the number of rows needed For e.g., 5
Second line onwards you should enter the alphabets.
For e.g.,
a
b
c
d
e
"""

n = int(input())  # Number of rows
letters = [input() for _ in range(n)]  # List of letters
# Loop through each row
for i in range(n):
    row = []  # Initialize the row list
    # Loop through each letter up to the current row number
    for j in range(i+1):
        row.append(letters[j] + ' ')  # Add the letter and a space to the row list
    # Add the remaining spaces to the end of the row
    for k in range(n-i-1):
        row.append('')  # Add two spaces to the row list
    print(''.join(row))  # Print the row as a string, joining the letters and spaces with no separator