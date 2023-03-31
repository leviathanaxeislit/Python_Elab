"""Question description
Sudan wants to find the factorial of a given number. Can you help him to calculate the factorial of a number (a non-negative integer) using Function. The function accepts the number as an argument.
Function Description
The factorial of 4 is 4x3x2x1=24
Constraints
0≤n≤500
Input Format: Refer test cases
Output Format:
Refer test cases

Logical Test Cases
Test Case 1
INPUT (STDIN)
4
EXPECTED OUTPUT
24
Test Case 2
INPUT (STDIN)
5
EXPECTED OUTPUT
120

Mandatory Test Cases
Test Case 1
KEYWORD
def
Test Case 2
KEYWORD
if
Test Case 3
KEYWORD
else"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))