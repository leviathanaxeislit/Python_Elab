"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2n ?
"""

def calculate(n, power):
    return sum([int(i) for i in str(pow(n, power))])
n = 2
power = int(input(''))
print (calculate(n, power))