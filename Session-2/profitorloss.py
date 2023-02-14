"""Problem Description:
Aarav a newbie entrepreneur was studying the profit and loss of his company.
He found out for some products cost price is greater than selling price, there was some loss and for other products he got some profit
Can you kindly automate this small work for him by creating a code that checks what arav wants? 
Constraints: 
30 <= cp<= 50,
30 <= sp<= 50 
If Cost Price > Selling Price then its "Loss"
If Cost Price < Selling Price then its  "Profit"
If Cost Price = Selling Price then its  "No Profit No Loss".
Input Format:
First Line : Integer representing the Cost price
Second Line: Integer representing Selling Price
Output Format:
Print Profit , Loss or No Profit No Loss Based on the condition."""

cp = int(input())
sp = int(input())

if cp > sp:
    print("Mislay")
elif cp < sp:
    print("Profit")
else:
    print("No Profit No Mislay")
