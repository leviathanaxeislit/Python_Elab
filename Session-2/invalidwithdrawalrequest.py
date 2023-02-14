"""
Question Description:
Atifa would like to withdraw X ₹INR from an ATM. 
The cash machine will only accept the transaction if X is a multiple of 5, and Atifa's account balance has enough cash to perform the withdrawal transaction (including bank charges). 
For each successful withdrawal, the bank charges 0.5 ₹INR. 
Functional Description:
Calculate and display the Atifa's account staus after the transaction based on the following condition:
If the amount requested   >  the available initial balance - bank charges and or if the requested amount is not the multiple of 5
In the First Line of Output Print as “Invalid Withdrawal Request”
In the Second Line of Output Print the Initial Balance with two values after decimal point.
If the amount requested   ≤ to the available initial balance - bank charges and if the requested amount is not the multiple of 5
In the First Line of Output Print the Current balance after the successful transaction with two values after decimal point.
In the Second Line of Output Print the Initial Balance with two values after decimal point.
"""
requested_amount = int(input())
initial_balance = float(input())
bank_charges = 0.5
if requested_amount % 5 != 0 or requested_amount > initial_balance - bank_charges:
    print("Invalid Withdrawal Request")
    print("Initial Balance : {:.2f}".format(initial_balance))
else:
    current_balance = initial_balance - requested_amount - bank_charges
    print("Current Balance : {:.2f}".format(current_balance))
    print("Initial Balance : {:.2f}".format(initial_balance))
