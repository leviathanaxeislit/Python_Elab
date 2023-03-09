"""
Euler asked the question to Ramanujan that, from the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is ____. Can you help Ramanujan to answer the sum of these multiples ?
Function description
Upper limit of natural number should be get from the user and store it to the variable N.
Constraints
10≤N≤1000
Input Format:
Single line input which represent the natural number
Output Format:
The sum of these multiples will be displayed.

Logical Test Cases
Test Case 1
INPUT (STDIN)
10
EXPECTED OUTPUT
23
Test Case 2
INPUT (STDIN)
15
EXPECTED OUTPUT
45
Input: 10
Output: 23

Input: 15
Output: 45
"""
def sum_of_multiples(N):
    total = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
N = int(input()) # get input from user
print(sum_of_multiples(N)) # calculate and print the sum of multiples
