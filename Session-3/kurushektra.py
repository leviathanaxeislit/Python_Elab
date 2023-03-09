"""Question Description
In the battle of Kurukshetra, The various vyuhas were studied by the Kauravas and Pandavas alike. Most of them can be beaten using a counter-measure targeted specifically against that formation. In the form of battle described in the Mahabharata, it was important to place powerful fighters in positions where they could inflict maximum damage to the opposing force, or defend their own side. As per this military strategy, a specific stationary object or a moving object or person could be captured, surrounded and fully secured during battle. In order to form the triangle pattern by Pandavas, can you help them to make a program for the pyramid pattern?  
Constraints
Use only for loop
Input Format:
Number of rows will be given as an integer. For example If 7 is entered, then the output will be as in the below output format 
Output Format:
*******
******
*****
****
***
**
*"""
n = int(input()) # get input from user

# iterate over each row in reverse order
for i in range(n, 0, -1):
    # print the appropriate number of stars for this row
    for j in range(i):
        print("*", end="")
    print() # move to the next line


n = int(input()) # get input from user

# iterate over each row
for i in range(n):
    # print the appropriate number of stars for this row
    for j in range(i+1):
        print("* ", end="")
    print() # move to the next line
