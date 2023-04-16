"""Problem Description:
Aaron has a number D containing only digits 0's and 1's. He wants to make the number to have all the digits same. For that, he will change exactly one digit, i.e. from 0 to 1 or from 1 to 0. 
If it is possible to make all digits equal (either all 0's or all 1's) by flipping exactly 1 digit then output "Yes", else print "No" (quotes for clarity)
Constraints:
1 ≤ T ≤ 10
1 ≤ Length of the number D ≤ 10
Input Format:
The first line will contain an integer 'T' representing the number of test cases.
Each test case contain a number made of only digits 1's and 0's on newline
Output Format:
Print T lines with a "Yes" or a "No", depending on whether its possible to make it all 0s or 1s or not.

Logical Test Cases
Test Case 1
INPUT (STDIN)
3
1010
101
100
EXPECTED OUTPUT
NO
YES
Test Case 2
INPUT (STDIN)
6
010
1101
0011
101110
0001
0010
EXPECTED OUTPUT
YES
NO
NO
YES"""

def check_all_same(s):
    # Count number of 0s and 1s
    count_0 = s.count('0')
    count_1 = s.count('1')
    
    # If all digits are already same, return Yes
    if count_0 == len(s) or count_1 == len(s):
        return "YES"
    # If there is only one 0 or one 1, return Yes
    if count_0 == 1 or count_1 == 1:
        return "YES"
    # If there is more than one 0 and more than one 1, return No
    if count_0 > 1 and count_1 > 1:
        return "NO"
    # If there is exactly one 0 and more than one 1, or exactly one 1 and more than one 0, return Yes
    else:
        return "YES"
if __name__ == "__main__":
    # Get number of test cases
    T = int(input())
    # Loop over all test cases
    for i in range(T):
        # Get input string
        s=str(input())
        # Call function to check if all digits can be made same by flipping one digit
        result = check_all_same(s)
        # Print the result
        print(result)