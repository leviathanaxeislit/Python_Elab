"""Sajid was booking a train ticket from Chennai to Delhi for his family. Two of the relatives was interested in joining that journey from different places with their family members 
But, Sajid can book one ticket out of those persons also along with his family members. 
He wants to identify the right person to book the train ticket.
These two persons are college students, so he decided to conduct a small coding test to finalize the person who wants to travel with his family members.
Sajid created one of the basic level questions such that the two persons need to identify the area and the perimeter for the given rectangle. 
Can you help?
Mandatory: 
Must use "class rectangle:"
Input: 
The first line contains the length of the rectangle and the second line contains the breadth of it. 
Output: 
Print the area in the first line and the perimeter in the second.                                    

Logical Test Cases
Test Case 1
INPUT (STDIN)
10
20
EXPECTED OUTPUT
The area is: 200.0
The perimeter is: 60.0
Test Case 2
INPUT (STDIN)
34
20
EXPECTED OUTPUT
The area is: 680.0
The perimeter is: 108.0

Mandatory Test Cases
Test Case 1
KEYWORD
class rectangle:"""
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
# User Input
length = float(input())
breadth = float(input())
# Output
r = rectangle(length, breadth)
print("The area is:", r.area())
print("The perimeter is:", r.perimeter())