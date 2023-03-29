"""
Problem Description:
Akash the die heart fan of AR Rahman went to the live concert happened in Bangalore with his family members.
The event management firm responsible for the event arranged the seats for the audience in descending order of maximum number of tickets booked for single family.
As per the seating arrangement family with the highest number of people are allotted the seats in the front rows and the family with the lowest number of people are allotted the seats in the last row.
For the convenience of the seating arrangement volunteers to know how many seat need to be positioned in each row the event management firm have planned to develop the software which displays the exact seat layout if the total number of rows is provided.
Can you help them with the logic of doing so?
Constraints:
1 ≤ nooffamilymembers ≤ 20
Input Format:
Only line of input has single integer representing the total number of rows for the concert.
Output Format:
Print the seating arrangement layout based on the number of rows provided.
Refer sample testcases for format specification.

Logical Test Cases
Test Case 1
INPUT (STDIN)
11
EXPECTED OUTPUT
11 11 11 11 11 11 11 11 11 11 11 
10 10 10 10 10 10 10 10 10 10 
9 9 9 9 9 9 9 9 9 
1
Test Case 2
INPUT (STDIN)
8
EXPECTED OUTPUT
8 8 8 8 8 8 8 8 
7 7 7 7 7 7 7 
6 6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1"""

num_rows = int(input())

for i in range(num_rows):
    num_seats = num_rows - i
    row_layout = [num_seats] * num_seats
    print(*row_layout, end=" ")
    print()