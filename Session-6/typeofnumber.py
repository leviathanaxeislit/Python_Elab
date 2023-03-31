"""
Question description
Nathan was a student by morning and a computer nerd by night 
At the earlier stages of his career, he was in need of money,
So he started working in a grocery store, parallelly he did many part-time jobs for daily wages. one day his part-time class teacher asked a question, Nathan has to identify if the number entered by the user is positive, negative, or zero. 
Constraints:
1 < n < 100000
INPUT: 
the first line contains the number.
OUTPUT: 
it displays whether it is positive, negative or zero.

Logical Test Cases
Test Case 1
INPUT (STDIN)
5
EXPECTED OUTPUT
+ve
Test Case 2
INPUT (STDIN)
-5
EXPECTED OUTPUT
-ve
"""
class check:
    def check(self):
        # take input from user
        n = int(input())
        if n > 0:
            print("+ve")
        elif n < 0:
            print("-ve")
        else:
            print("0")
# create an object of the class and call the check method
c = check()
c.check()