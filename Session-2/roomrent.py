"""Problem Description:
Aadi and Tara travel frequently around the world.
Since most of their travels are unplanned they usually book the rooms for stay nearer to the locality they are going to visit.
Functional Description:
In most of the tourist places the room rent is 20% high during peak seasons [April and May]. 
Can you help them with the Room Rent Estimation Portal using flow control concept that provides the total rent to pay if the details such as Month,Room Rent and Total days of stay are provided? 
Constraints:
1≤month≤12
500≤roomrent≤5000
1≤numofdays≤15
Input Format:
The first line of the input has a single integer which corresponds to the number of the month. [ Ex. January is 1, and March is 3]. 
The second line of the input has a single floating point number which corresponds to the room rent per day. 
The third line of the input has a single integer which corresponds to the number of days stayed in the hotel.
Output Format:
Print the total room rent to be paid with two values after decimal point. 
Refer sample testcases for Format Specification."""

month = int(input())
room_rent = float(input())
num_of_days = int(input())

if month == 4 or month == 5:
    total_rent = room_rent * num_of_days * 1.2
else:
    total_rent = room_rent * num_of_days

print("Rs.{:.2f}".format(total_rent))
