"""Problem Description:
Selvan is working as a QC in a reputed Multinational Conglmerate. 
His task is to check if the given Keyboard has a valid alphabets. 
But since many Keyboards are need to be verified, he is finding is difficult to finish the task. 
Can you automate the checking process and reduce his work load?
Constraints: 
a <= ch <= z
A <= ch <= X
1 <= ch <= 500
Input Format:
Only line of input has the single input that needs to be checked. It can be a character a-z or A-Z or a number
Output Format 
If it is an Alphabet print ALPHABET else print NOT AN ALPHABET."""

ch = input()

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("ALPHABET")
else:
    print("NOT AN ALPHABET")
    