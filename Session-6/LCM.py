"""Dr. Ramesh is a professor at a university. He is eager to put on a show for pupils as well. During his lunch break, he decided to host a mind-body activity.
He needs to ask a few thought-provoking questions.
He invited participants to answer questions such that, The program takes two numbers and prints the LCM of two numbers.
Mandatory: the name of the object must be 'obj' and the name of the class must be 'lcm'
Can you help?
Constraints:
1 < N < 10^5
INPUT: 
first-line represents the number
The next Line represents the second input value 
OUTPUT: 
The single line represents the LCM of the given inputs.

Logical Test Cases
Test Case 1
INPUT (STDIN)
5
5
EXPECTED OUTPUT
LCM is: 5
Test Case 2
INPUT (STDIN)
7
8
EXPECTED OUTPUT
LCM is: 56

use these keywords in the program
KEYWORD
class lcm:

KEYWORD
while(1)
"""
class lcm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_lcm(self):
        i = 1
        while(1):
            if(i % self.a == 0 and i % self.b == 0):
                lcm = i
                break
            i += 1
        print("LCM is:", lcm)

obj = lcm(int(input()), int(input()))
obj.find_lcm()