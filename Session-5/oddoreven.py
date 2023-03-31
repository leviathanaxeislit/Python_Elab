"""Question description
Sudan had a task for the seating arrangements to filter the even roll number for giving the course certificates to the even roll numbered peoples. Can you help him to check the even number using function.
Constraints
0≤n≤10000000000
Input Format:
Refer the test case
Output Format:
Refer the test case

Logical Test Cases
Test Case 1
INPUT (STDIN)
43
EXPECTED OUTPUT
ODD
Test Case 2
INPUT (STDIN)
44
EXPECTED OUTPUT
Even

Mandatory Test Cases
Test Case 1
KEYWORD
def
Test Case 2
KEYWORD
%2"""
def check_even(n):
    if n %2 == 0:
        return "Even"
    else:
        return "ODD"
n = int(input())
print(check_even(n))