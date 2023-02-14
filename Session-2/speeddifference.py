"""
Problem Description:
Arav and Aaron are participating in the Bike racing. Arav have crossed some milestores earlier and Aaron crossed some milestores earlier during their racing,because they have changed their speeds at different times.
Both of them like to know the difference in speeds between them at different stages of racing.
Can you help finding the speed difference between Arav and Aaron?
Constraints:
20≤ aravspeed ≤100
20≤ aaronspeed ≤100
Input Format: 
The first line of input represents the speed of Arav. 
The second line of input represents the speed of Aaron. 
Output Format: 
Print difference between the driving speed of two participants in a single line.
"""
# Read input as sepcified in the question.
# Print output as specified in the question.

arav_speed = int(input())
aaron_speed = int(input())
if arav_speed > aaron_speed:
    speed_diff = arav_speed - aaron_speed
    print(speed_diff)
elif aaron_speed > arav_speed:
    speed_diff = aaron_speed - arav_speed
    print(speed_diff)
else:
    print(0)

