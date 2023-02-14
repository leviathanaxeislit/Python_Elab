"""Problem Description:
Laasya looking at the friends birthday list on a social media site likes to find if the particular person's birthday year is a leap year or not. 
Since many will have the same doubt she decides to automate the task by writing the code snippet for finding the same but she don't know the logic to write it. 
Can you help Laasya to accomplish her task? 
Constraints: 
1 <= year<= 10000
Input Format: 
The Single Line containing the integer value representing year.
Output Format: 
Print as either NOT A LEAP YEAR or LEAP YEAR after checking the year."""

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
