"""Question description:
Yasir is a very active young man who is very interested in making money in a simple way. 
So he is always looking for a way to make some money. 
One day, a money-making show called Jackpot on popular channel news came to Yasir's ears. 
So he was going to the JACKPOT game in a game park it has a dial full of numbers in random order.
If it is arranged in ascending order using the sorting concept, he will win a million-dollar prize. 
can you help him to input an array and sort it in ascending order?
Input Format:
First--line indicates the random integer numbers.
Output Format:
In a single-line of output print the values in ascending order.

Logical Test Cases
Test Case 1
INPUT (STDIN)
8 5 0 2
EXPECTED OUTPUT
0 2 5 8
Test Case 2
INPUT (STDIN)
8 5 0 2 1 3 7 6 6 11
EXPECTED OUTPUT
0 1 2 3 5 6 6 7 8 11

Mandatory Test Cases
Test Case 1
KEYWORD
input
Test Case 2
KEYWORD
for"""
# Read the input
arr = list(map(int, input().split()))

# Sort the array in ascending order using a for loop
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

# Print the sorted array
print(*arr)