"""
 Athika and Ritu got a nice job at a MNC company . She was confused with the salary credited in her account. 
To verify if the correct amount of HRA and DA was provided to them.
Ritu and Athika planned to develop a software that calculates the salary pay if the basic pay was provided. 
The Salary policy of Athika and Ritu's Company is as follows: HRA is 80% of the basic pay and DA is 40% of basic pay. 
Can you help Ritu and Athika in the software development? 
Constraints
20000≤basic≤75000
Input Format
Single Integer representing the basic pay of the employee.
Output Format
Print the Gross salary of employee by adding the certain amount of HRA and DA to the basic pay and correcting to 2 decimal places.

"""

bpa = float(input(''))
hra = bpa*0.8
da = bpa*0.4
total = hra+da+bpa
print('{:.02f}'.format(total))
