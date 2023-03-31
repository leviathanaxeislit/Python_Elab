"""
Question description
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:
string s: the string to modify
Input Format
A single line containing a string s.
Output Format
string: the modified string

Logical Test Cases
Test Case 1
INPUT (STDIN)
Care Presents Pythonist 3
EXPECTED OUTPUT
cARE pRESENTS pYTHONIST 3
Test Case 2
INPUT (STDIN)
CARE
EXPECTED OUTPUT
care
"""
def swap_case(s):
    """
    This function takes a string as input and swaps the case of all characters in the string.
    """
    swapped_str = ""
    for char in s:
        if char.isupper():
            swapped_str += char.lower()
        elif char.islower():
            swapped_str += char.upper()
        else:
            swapped_str += char
    return swapped_str

# Taking user input
s = input()

# Calling the swap_case function with user input
print(swap_case(s))