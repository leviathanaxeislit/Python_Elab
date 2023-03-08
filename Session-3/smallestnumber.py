"""Question description
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Constraints
100≤n≤1000
Input Format: 
Refer the logical test cases
Output Format:
Refer the logical test cases

Logical Test Cases
Test Case 1
INPUT (STDIN)
20
EXPECTED OUTPUT
232792560
Test Case 2
INPUT (STDIN)
10
EXPECTED OUTPUT
2520"""

def smallest_multiple(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = 1
    for prime in primes:
        power = 1
        while prime**power <= n:
            power += 1
        result *= prime**(power-1)
    return result

n = int(input())
print(smallest_multiple(n))
