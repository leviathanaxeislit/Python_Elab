"""Question description:
Selvan asks his friend Arav to buy the book. Arav would recommend a bookstall in Thanjavur. Arav further says that the advice given to Selvan is to have the number ISBN when buying the book. Selvan doesn't know what it is. Arav tells him that. You must have notices every book has a 10 digit series of number. 
An ISBN (International Standard Book Number) is a 10 digit number that is used to identify a book. The first nine digits of the ISBN number are used to represent the Title, Publisher, Group of the book, and the last digit is used for checking whether ISBN is correct or not. 
The first 9 digits of it, can take any value between 0 and 9, but the last digits, sometimes may take a value equal to 10; this is done by writing it as ‘X’. 
 
Functional Description:
To verify an ISBN, calculate 10 times the first digit, plus 9 times the second digit, plus 8 times the third digit, and so on until we add 1 time the last digit. If the final number leaves no remainder when divided by 11, the code is a valid ISBN.
Constraints:
1≤=t≤=10 
1≤=isdn≤1000
Input Format: 
The line with an integer indicates  the number of books 
The second input as a character for ISDN number 
Output Format: 
Print as “Valid” or “Invalid” based on the ISBN value given as input.

Logical Test Cases
Test Case 1
INPUT (STDIN)
1
00750142X612
EXPECTED OUTPUT
Invalid
Test Case 2
INPUT (STDIN)
3
007462542X
007562642X
018462553X
EXPECTED OUTPUT
Valid
Valid"""
def validate_isbn(isbn):
    if len(isbn) != 10: # ISBN should be a 10 digit number
        return "Invalid"
    else:
        total = 0
        for j in range(10):
            if isbn[j] == 'X': # handle the case where last digit is 'X'
                total += 10 * (10-j)
            else:
                total += int(isbn[j]) * (10-j)
        if total % 11 == 0:
            return "Valid"
        else:
            return "Invalid"

t = int(input()) # number of books
for i in range(t):
    isbn = input()
    print(validate_isbn(isbn))