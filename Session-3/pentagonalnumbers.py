"""Question description
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. Generate the first n pentagonal numbers.
Constraints
1≤n≤100
Input Format: 
Refer the test case
Output Format:
Refer the test case"""

# Prompt for user input
n = int(input())
# Generate the first n pentagonal numbers
for i in range(1, n):
    # Calculate the i-th pentagonal number using the formula Pn=n(3n−1)/2
    Pn = int( (i * (3 * i - 1)) / 2)
    # Print the i-th pentagonal number
    print(Pn)
    