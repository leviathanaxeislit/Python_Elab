"""Question description
Sudan and Siva are school mates. They challenge each other to play a game that to arrange string characters such that lowercase letters should come first
Constraints
1<t<5
Input Format:
Refer the test cases
Output Format:
Refer the test cases

Logical Test Cases
Test Case 1
INPUT (STDIN)
2
Radhakrishnan
Radhai
EXPECTED OUTPUT
adhakrishnanR
adhaiR
Test Case 2
INPUT (STDIN)
4
Saravanan
Manikandan
Vignesh
Subash
EXPECTED OUTPUT
aravananS
anikandanM
igneshV
ubashS"""

# Taking input for the number of test cases
t = int(input())
# Looping through each test case
for i in range(t):
    # Taking input for the string
    str1=str(input())
    
    # Sorting the characters in the string using the sorted() function and the key parameter
    sorted_string = sorted(str1, key=lambda x: x.isupper())
    
    # Joining the sorted characters back to form the final string
    final_string = ''.join(sorted_string)
    
    # Printing the final string
    print(final_string)