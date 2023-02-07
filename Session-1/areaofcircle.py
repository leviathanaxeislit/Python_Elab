"""
Question description 
In geometry, the area enclosed by a circle of radius r is πr^2. Here the Greek letter π represents a constant, approximately equal to 3.142, which is equal to the ratio of the circumference of any circle to its diameter. Subash wants to find the area of circle for the given radius. Can you help him to calculate the area of circle for the given radius? 
Constraints 
Subash has to declare the radius named as r with float datatype and pi as 3.142 without importing math 
Input Format
Refer the Testcases 
Output Format
Use str()  to print the output. Refer the Testcases. 
 """
r = float(input(""))
pi = 3.142
area = pi * r**2
print("The area of the circle with radius",r,"is:",area)