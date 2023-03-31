"""Question description
Mahendran is a manager, he has assigned a task to Nathan.
Nathan is a purchase officer of this Financial organization. Nathan has given this task to a private company to design a computer keyboard for a Financial organization.
the private vendor company has delivered the product to Nathans office.  
Nathan and the workers have tested the keyboard working condition. every part of the keyboard was perfect but when you press the on keys "7", it was replaced with "zero" and vice versa. 
Now purchase officer Nathan decided to return the product to a Private design company to correct the errors. can you help the designer to rectify the errors?
You have to make a program to replace the number "7" where the “0” is present in the given number. then the company members will do the necessary steps to rectify the issue.
Constraints
1≤num≤1000
Input
Get the input represents “num” 
Output
Print the output where zero is replaced by 7

Logical Test Cases
Test Case 1
INPUT (STDIN)
10101
EXPECTED OUTPUT
17171
Test Case 2
INPUT (STDIN)
100100
EXPECTED OUTPUT
177177

Mandatory Test Cases
Test Case 1
KEYWORD
str
Test Case 2
KEYWORD
replace"""
def replace_digits(num_str):
    return num_str.replace('0', 'x').replace('7', '0').replace('x', '7')

input_str = str(input().strip())
print(replace_digits(input_str))