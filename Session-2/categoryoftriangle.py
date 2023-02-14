"""Problem  Description:
Simon was working in a Casa Grande. 
His superior officer ordered him to construct a new building by incorporating equilateral, scalene and isosceles triangular shapes wherever possible. 
But he has no idea about equilateral, scalene and isosceles triangle. 
Can you clarify his doubt by giving him the correct category of triangle based on the values of sides given by simon?
Functional Description :
If All the Sides are Equal then it is a Equilateral Triangle
If two Sides are Equal then it is a Isosceles Triangle
If no Sides are Equal then it is a Scalene Triangle
Constraints:
1<=side1<=100
1<=side2<=100
1<=side3<=100
Input Format:
Each line has values of type integer separated by enter key representing 'side1','side2' and 'side3'.
Output Format:
Print as either equilateral or scalene or isosceles triangle based on the values of the sides."""

side1 = int(input())
side2 = int(input())
side3 = int(input())
if side1 == side2:
    if side2 == side3:
        print("Equilateral triangle")
    else:
        print("Isoceles triangle")
elif side1 == side3:
    print("Isoceles triangle")
elif side2 == side3:
    print("Isoceles triangle")
else:
    print("Scalene triangle")