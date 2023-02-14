"""
Problem Description:
The Election Commission of India distributed the voter ID to all eligible citizens. 
But Amira didn't received a Voter ID on time. 
So, she gets confused about her eligibility for voting?
Can you clarify her doubt?
Condition for Eligibility as per Election Commission of India is 
(i) Eligible if age >=18
(i) Not Eligible if age <18
Constraints : 
1≤age≤100
Input Format:
The only line of input has single value of type integer representing age.
Output Format:
Print as Eligible or Not Eligible based on the eligibility criteria in a single line. Refer the Testcases.
"""


age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
