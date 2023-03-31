"""You are given a spreadsheet that contains a list of athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.
(Image: image)
Note that is indexed from to , where is the number of attributes.
Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
Input Format
The first line contains N and  M separated by a space.
The next N lines each contain M elements.
The last line contains K.
Constraints
1≤N,M≤1000
0≤K<M
Each element≤1000
Output Format
Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Logical Test Cases
Test Case 1
INPUT (STDIN)
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Test Case 2
INPUT (STDIN)
5 2
10 2
7 1
9 9
1 23
6 5
1

EXPECTED OUTPUT
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

EXPECTED OUTPUT
7 1
10 2
6 5
9 9
1 23"""

n, m = map(int, input().strip().split(' '))

# read the data into a list of tuples
data = []
for i in range(n):
    row = tuple(map(int, input().strip().split(' ')))
    data.append(row)

# sort the data based on the k-th attribute
k = int(input().strip())
data = sorted(data, key=lambda x: x[k])

# print the sorted data
for row in data:
    print(" ".join(map(str, row)))