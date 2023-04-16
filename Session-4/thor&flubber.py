"""Question description
Thor and Flubber have the task is to check whether the string has at least one letter(character) and one number. Return “True” if the given string full fill above condition else return “False” (without quotes).
Can you help them to finish the task?
Constraints
t-represents the number of testcases.
1≤t≤5
Input Format:
Refer Test cases
Output Format
Refer Test cases

Logical Test Cases
Test Case 1
INPUT (STDIN)
1
radha82
EXPECTED OUTPUT
True
Test Case 2
INPUT (STDIN)
2
radha
rajiv19
EXPECTED OUTPUT
False
True"""

# Read the number of testcases
t = int(input())
# Loop through all the testcases
for i in range(t):
    # Read the input string
    str1=str(input())
    # Check if the string has at least one letter and one number
    if any(c.isalpha() for c in str1) and any(c.isdigit() for c in str1):
        print("True")
    else:
        print("False")