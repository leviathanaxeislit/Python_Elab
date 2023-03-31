"""Question description
Ramesh was booking a train ticket from Chennai to Delhi for his family. Two of the relatives was interested in joining that journey from different places with their family members 
But, Ramesh can book one ticket out of those persons also along with his family members. 
He wants to identify the right person to book the train ticket.
These two persons are college students, so he decided to conduct a small coding test to finalize the person who wants to travel with his family members.
Ramesh created one of the basic level questions for calculating the area of a circle using class and objects concepts.
you have to write the program to take the radius from the user and finds the area & perimeter of the circle using classes. 
Also check if the entered radius is negative.
If yes, display "Enter a valid radius" message.
Constraints:
1 < R < 100000
INPUT Format:
contains the radius of the circle.
OUTPUT Format:
the first line contains the area of the circle and the second line contains the perimeter of the circle.
               

Logical Test Cases
Test Case 1
INPUT (STDIN)
10
EXPECTED OUTPUT
Area of circle: 314.16
Perimeter of circle: 62.83
Test Case 2
INPUT (STDIN)
-5
EXPECTED OUTPUT
Enter a valid radius

Mandatory Test Cases
Test Case 1
KEYWORD
class circle():
Test Case 2
KEYWORD
def area(self):"""

import math
class circle():
    def __init__(self, radius):
        self.radius = radius
    
    def is_valid_radius(self):
        return self.radius > 0
    
    def area(self):
        if not self.is_valid_radius():
            return "Enter a valid radius"
        else:
            return round(math.pi * self.radius**2, 2)
    
    def perimeter(self):
        if not self.is_valid_radius():
            return "Enter a valid radius"
        else:
            return round(2 * math.pi * self.radius, 2)
radius = int(input())
c = circle(radius)
if not c.is_valid_radius():
    print("Enter a valid radius")
else:
    print("Area of circle:", c.area())
    print("Perimeter of circle:", c.perimeter())