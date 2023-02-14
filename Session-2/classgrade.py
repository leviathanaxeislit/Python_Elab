
s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
total=s1+s2+s3+s4+s5
avg=total/5
print("{:.2f}".format(avg),"Percent")
if avg>=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60:
    print("Grade D")
elif avg>=40:
    print("Grade E")
else:
    print("Grade F")
