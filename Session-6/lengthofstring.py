"""Rani and Raji are sisters they love to compete by playing math games which gradually helped them in their academics one day.
rani gave her a task to her sister.
The task involves a string e program takes a string and calculates the length of the string without using library functions.
Mandatory: must use the function name as "def find(self):" and should use object name as "L" and should also use "L.find()"
But raji thought she can code a program for this concept but she is finding it difficult.
Can you help her with the suitable logic?
Constraints:
1 < string length < 1000
INPUT: 
the first line contains the string.
OUTPUT: 
print the result as output.

Logical Test Cases
Test Case 1
INPUT (STDIN)
orange
EXPECTED OUTPUT
Length of the string is:
6
Test Case 2
INPUT (STDIN)
apple
EXPECTED OUTPUT
Length of the string is:
5

use the keywords
KEYWORD
class length:

KEYWORD
def find(self):

KEYWORD
L.find()"""
class length:
    def __init__(self, string):
        self.string = string
        
    def find(self):
        count = 0
        for char in self.string:
            count += 1
        print("Length of the string is:")
        print(count)

string = input()
L = length(string)
L.find()