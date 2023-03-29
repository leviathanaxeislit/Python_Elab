"""
Question description
Thanos and iron man had a challenge  to get the stones from Hulk. But Hulk gave the task to them. They need to display the even and odd numbers separately from the numbers.
Input Format:
First value is the size of the array.
Second value onwards the numbers which will be separated as even and odd.

Logical Test Cases
Test Case 1
INPUT (STDIN)
3
22
50
11
EXPECTED OUTPUT
22 50 
11
Test Case 2
INPUT (STDIN)
5
2
4
6
5
1
EXPECTED OUTPUT
2 4 6 
5 1
"""
n = int(input())
even = []
odd = []
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(*even, end=' ')
print()
print(*odd, end=' ')
print()