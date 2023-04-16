"""Question description
Janaki had the extra ability that, she will spell the given set of strings in reverse order. Can you verify the strings?
Constraints
1≤t≤5
Input Format
Refer the test cases
Output Format
Refer the test cases

Logical Test Cases
Test Case 1
INPUT (STDIN)
2
Raja
Radha
EXPECTED OUTPUT
ajaR
ahdaR
Test Case 2
INPUT (STDIN)
3
President
Prime Minister
Governor
EXPECTED OUTPUT
tnediserP
retsiniM emirP
ronrevoG"""

# Prompt inputs
t=int(input())
# Loop through each test case
for i in range(t):
    # Get the string
    test_string=str(input())
    
    # Reverse the string
    string_reversed = test_string[::-1]
    
    # Print the reversed string
    print(string_reversed)