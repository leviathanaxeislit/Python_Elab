"""Question description
Rani and Raji are sisters they love to compete by playing math games which gradually helped them in their academics one day.
rani gave her a task to her sister.
The task involves a string and removes the characters of odd index values in the string.
The task should be completed by using class and objects in python concept.
But raji thought she can code a program for this concept but she is finding it difficult.
Can you help her with the suitable logic?
Mandatory: the name of the class must be "index" 
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
Modified string is:
oag
Test Case 2
INPUT (STDIN)
apple
EXPECTED OUTPUT
Modified string is:
ape

use these keywords in the program
KEYWORD
class index:

KEYWORD
def modify(self):"""
class index:
    def __init__(self, string):
        self.string = string
        
    def modify(self):
        modified_string = ""
        for i in range(len(self.string)):
            if i % 2 == 0:
                modified_string += self.string[i]
        print("Modified string is:\n" + modified_string)
input_string = input()
string_obj = index(input_string)
string_obj.modify()