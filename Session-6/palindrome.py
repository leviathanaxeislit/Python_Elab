"""Question description
Nathan was a student by morning and a computer nerd by night 
At the earlier stages of his career, he was in need of money,
So he started working in a grocery store, parallelly he did many part-time job for daily wages. one day his part-time class teacher asked a question, Nathan has to identify the palindrome as a string which is the same read forward or backward. The program takes a string as input and checks if it is a palindrome. 
Constraints:
1 < n < 100000
Mandatory: the name of the reverse function must be "reversecheck"
INPUT: 
the first line contains the string to be checked.
OUTPUT: 
it displays whether the string is palindrome or not.

Logical Test Cases
Test Case 1
INPUT (STDIN)
51
EXPECTED OUTPUT
It is not palindrome
Test Case 2
INPUT (STDIN)
515
EXPECTED OUTPUT
It is palindrome

Mandatory Test Cases
Test Case 1
KEYWORD
class string:
Test Case 2
KEYWORD
def reversecheck(self):"""

class string:
    def __init__(self, s):
        self.s = s
    
    def reversecheck(self):
        # Reversing the string using slicing
        rev = self.s[::-1]
        
        # Checking if the reversed string is equal to the original string
        if self.s == rev:
            print("It is palindrome")
        else:
            print("It is not palindrome")
            
# Reading the input string from the user
s = input()
# Creating an object of the string class
str_obj = string(s)
# Calling the reversecheck method to check if the string is palindrome
str_obj.reversecheck()