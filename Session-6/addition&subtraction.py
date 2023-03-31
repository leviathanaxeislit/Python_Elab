"""Question description:
Adam has two numbers and he wants to find the sum and difference of them, but he is not sure how he can do so. 
Can you help him solve this particular problem
Constraints:
1≤ A ≤ 1000
1≤ B ≤ 1000
Input Format:
First line of input has a single value of type integer representing the first number
Second line of input has a single value of type integer representing the second number
Output Format:
In the First line of output print the sum of the two input numbers.
In the Second line of output print the difference between the two input numbers.

Logical Test Cases
Test Case 1
INPUT (STDIN)
95
15
EXPECTED OUTPUT
110
80
Test Case 2
INPUT (STDIN)
115
20
EXPECTED OUTPUT
135
95

use the keywords
KEYWORD
class Operation:

KEYWORD
def addition

KEYWORD
def subtraction
KEYWORD
int(input())"""
class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b

a = int(input())
b = int(input())

op = Operation(a, b)
sum = op.addition()
diff = op.subtraction()

print(sum)
print(diff)