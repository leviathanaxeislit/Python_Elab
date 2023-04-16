"""Question description
Janaki set the password of her locker that the possible set of substrings from the string. Can you help her to set the password?
Constraints
1<len(string)≤10
Input Format:
Refer the test cases
Output Format:
Refer the test cases

Logical Test Cases
Test Case 1
INPUT (STDIN)
abc
EXPECTED OUTPUT
a
c
Test Case 2
INPUT (STDIN)
abcd
EXPECTED OUTPUT
a
ab
abc
abcd
b
bc
bcd
c
cd
d"""

s=str(input())
# Printing all substrings of the string s
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])