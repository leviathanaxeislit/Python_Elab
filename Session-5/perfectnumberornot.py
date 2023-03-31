"""Question description
Darsh seemingly down-to-earth guy. Dash has a Brother Nathan. 
Nathan leads a life of a computer hacker by day and a thief by night. 
One day, Nathan tries to break the door digital lock of Darsh's room. 
Darsh who wants to prevent it thinks to give Passcode for security.
But it only accepts a perfect number as input. Can you help him to make a program for checking the given number is the perfect number or not…
Constraints
1≤ num ≤10000
Explanation
For example, 6 is a positive number that is completely divisible by 1, 2, and 3. We know that the number is also divisible by itself but we will include it in the addition of divisors. When we add these divisors (1 + 2 + 3 = 6), it produces 6, which is equal to the number that we have considered. So, we can say that 6 is a perfect number.
input Format
Get the single integer input “num”
Output Format
The single line that represents the given number is a perfect number or not a perfect number.
Refer sample input and output test cases.

Logical Test Cases
Test Case 1
INPUT (STDIN)
6
EXPECTED OUTPUT
Perfect Number
Test Case 2
INPUT (STDIN)
10
EXPECTED OUTPUT
Not a Perfect Number
"""
def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
num = int(input())
if is_perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")