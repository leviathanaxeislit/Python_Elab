"""Question description
Rani and Raji are sisters they love to compete by playing math games which gradually helped them in their academics one day.
rani gave her a task to her sister.
The task involves that the program takes kilometers as input and gives the output in miles.
Mandatory: the name of the input variable must be 'k' and the input must be accepted in the form of float. the name of the object must be 'm'.
But Raji thought she can code a program for this concept but she is finding it difficult.
Can you help her with the suitable logic?
Constraints:
1 < n< 1000000
INPUT: 
the first line contains the number of kilometers.
OUTPUT: 
print the output in miles.

Logical Test Cases
Test Case 1
INPUT (STDIN)
10
EXPECTED OUTPUT
10.0 kilometers is equal to 6.21371 miles
Test Case 2
INPUT (STDIN)
150
EXPECTED OUTPUT
150.0 kilometers is equal to 93.20565 miles

Use the keywords 

KEYWORD
class miles:

KEYWORD
def convert(self):

KEYWORD
m.convert()"""
class miles:
    def __init__(self, k):
        self.k = k
        
    def convert(self):
        miles = self.k * 0.621371
        print("{0} kilometers is equal to {1} miles".format(self.k, miles))
k = float(input())
m = miles(k)
m.convert()