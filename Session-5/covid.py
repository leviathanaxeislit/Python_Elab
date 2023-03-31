"""Question description
Finally, a COVID vaccine is out on the market and the Indian government has asked you to form a plan to distribute it to the public as soon as possible. There are a total of N people with ages a1,a2,…,aN.
There is only one hospital where vaccination is done and it is only possible to vaccinate up to D people per day. Anyone whose age is ≥80 or ≤9 is considered to be at risk. On each day, you may not vaccinate both a person who is at risk and a person who is not at risk. Find the smallest number of days needed to vaccinate everyone.
Constraints
1≤T≤10
1≤N≤104
1≤D≤105
1≤ai≤100 for each valid i
Input Format:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and D.
The second line contains N space-separated integers a1 ,a2,…,aN
Output Format:
         Required number will be displayed. Refer the test case.

Logical Test Cases
Test Case 1
INPUT (STDIN)
2
10 1
10 20 30 40 50 60 90 80 100 1
5 2
9 80 27 72 79
EXPECTED OUTPUT
10
3
Test Case 2
INPUT (STDIN)
1
5 1
10 20 30 40  1
EXPECTED OUTPUT
5

Mandatory Test Cases
Test Case 1
KEYWORD
import
Test Case 2
KEYWORD
ceil
"""
import math

# function to calculate the number of days required to vaccinate all people
def calculate_days_to_vaccinate_people(ages, max_vaccinations_per_day):
    num_people_at_risk = 0
    num_people_not_at_risk = 0

    # count the number of people who are at risk and not at risk
    for age in ages:
        if age >= 80 or age <= 9:
            num_people_at_risk += 1
        else:
            num_people_not_at_risk += 1

    # calculate the number of days required to vaccinate all people
    days_to_vaccinate_people = math.ceil(num_people_at_risk / max_vaccinations_per_day) + math.ceil(num_people_not_at_risk / max_vaccinations_per_day)

    return days_to_vaccinate_people

# main function to read input and calculate the number of days required to vaccinate all people
def main():
    t = int(input())

    for i in range(t):
        n, d = map(int, input().split())
        ages = list(map(int, input().split()))

        days_to_vaccinate_people = calculate_days_to_vaccinate_people(ages, d)

        print(days_to_vaccinate_people)

if __name__ == '__main__':
    main()