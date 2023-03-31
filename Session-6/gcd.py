"""Question description
Dr. Suresh is a professor at a university. He is eager to put on a show for pupils as well. During his lunch break, he decided to host a mind-body activity.
He needs to ask a few thought-provoking questions.
He invited participants to write the code for the questions such that, the program takes two numbers and prints the GCD of two numbers.
Mandatory: the name of the object must be 'g' and the name of the class must be 'gcd'
Constraints
0< n <10^5
Input Format
First-line represents number 1
Second-line represents number 2
Output Format
Single line prints the GCD number for given inputs

Logical Test Cases
Test Case 1
INPUT (STDIN)
5
5
EXPECTED OUTPUT
The GCD is 5
Test Case 2
INPUT (STDIN)
5
25
EXPECTED OUTPUT
The GCD is 5"""
import fractions
class gcd:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def g(self):
        return fractions.gcd(self.num1, self.num2)
    
num1 = int(input())
num2 = int(input())
obj = gcd(num1, num2)
print("The GCD is", obj.g())
