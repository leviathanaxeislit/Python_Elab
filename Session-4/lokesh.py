"""Problem Description:
Lokesh usually likes to play cricket, but now, he is bored of playing it too much, so he is trying new games with strings. 
Lokesh's friend Tina gave him binary strings S and R, each with length N, and told him to make them identical. 
However, unlike Tina, Lokesh does not have any superpower and Tina lets Lokesh perform only operations of one type: choose any pair of integers (i,j) such that 1≤i,j≤N and swap the i-th and j-th character of S. 
He may perform any number of operations (including zero).
For Lokesh, this is much harder than cricket and he is asking for your help. 
Tell him whether it is possible to change the string S to the target string R only using operations of the given type.
Constraints:
1≤T≤400
1≤N≤100
|S|=|R|=N
S and R will consist of only '1' and '0'
Input Format:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains a binary string S.
The third line contains a binary string R.
Output Format:
For each test case, print a single line containing the string "YES" if it is possible to change S to R or "NO" if it is impossible (without quotes).

Logical Test Cases
Test Case 1
INPUT (STDIN)
3
1000101
0110100
1101
0010
100111
010011
EXPECTED OUTPUT
YES
NO
Test Case 2
INPUT (STDIN)
4
6
100110
111010
9
001000101
111010010
7
0100010
1101011
5
10110
11010
EXPECTED OUTPUT
NO
NO
NO
YES"""
def can_be_identical(n, s1, s2):
    s1_count = s1.count('1')
    s2_count = s2.count('1')
    if s1_count != s2_count:
        return "NO"
    else:
        return "YES"
        
t = int(input())
for i in range(t):
    n=int(input())
    s1=str(input())
    s2=str(input())
    print(can_be_identical(n, s1, s2))