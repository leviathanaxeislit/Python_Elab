"""Problem Description:
Caleb and Irfan are purchasing apples which were priced according to their size. But their budget is minimum.
So they plan to choose one small, one medium and one large apple so that it will fit in their budget.
So can you help them choose the right apple by creating a logic by naming three apples they choose as apple1,apple2,apple3. 
Then check the condition if apple2 is greater than apple1 and apple3 is greater than apple2.
Constraints:
1≤ apple1 ≤600
1≤ apple2 ≤600
1≤ apple3 ≤600
Input format:
First Line: Single number of type integer representing the size of apple1
Second Line: Single number of type integer representing the size of apple2
Third Line: Single number of type integer representing the size of apple3
Output Format:
Print as “Fit into Budget” or “Doesn't fit into Budget” based on the condition."""

apple1 = int(input())
apple2 = int(input())
apple3 = int(input())
if apple2 > apple1 and apple3 > apple2:
    print("Fit into Budget")
else:
    print("Doesn't fit into Budget")
    