"""
Compute the area of a triangle when the lengths of all three sides are known. 
Let s1, s2 and s3 be the lengths of the sides. 
Let s = (s1 + s2 + s3)/2. 
Then the area of the triangle can be calculated using the following formula: 
area =sqrt(s × (s − s1) × (s − s2) × (s − s3)) 
Develop a program that reads the lengths of the sides of a triangle from the user and displays its area.
Function Description
area =sqrt(s × (s − s1) × (s − s2) × (s − s3))

"""
import math
s1=float(input())
s2=float(input())
s3=float(input())
s=(s1+s2+s3)/2
area =math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print('The area of triangle is {}'.format(area))