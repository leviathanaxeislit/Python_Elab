"""Question description:
Sajid is a graduate student he applied to a BPO company but he does not get typing fast. So he wanted to increase his typing speed for the job. 
His well-wisher suggested that he type the sentence "The quick brown fox jumps over the lazy dog" repeatedly. 
This sentence is known as a pangram because it contains every letter of the alphabet. 
After typing the sentence several times, Sajid needs to check whether the given number is a pangram.  can you help him, whether the given sentence is a pangram or not
 
Functional Description:
The for loop reads character by character of the String and if the character is an alphabet then increment the total if used[alphabet]=0 and it makes used[alphabet]=1 (increment for every new alphabet used between a to z. the alphabet count should not exceed 26.
Constraints:
The given input letters should be  a≤=str≤z 
Input Format : 
The only line of input has a input sentence.
Output Format : 
Print as “pangram” or “not a pangram” based on the condition

Logical Test Cases
Test Case 1
INPUT (STDIN)
The quick brown fox jumps over the lazy dog
EXPECTED OUTPUT
panagram
Test Case 2
INPUT (STDIN)
Thus the Entered String is a Pangram String
EXPECTED OUTPUT
not a panagram

Mandatory Test Cases
Test Case 1
KEYWORD
str
Test Case 2
KEYWORD
lower
Test Case 3
KEYWORD
if
"""
def is_pangram():
    # Read input sentence
    sentence = input("Enter a sentence: ").lower()

    # Initialize a list to keep track of used alphabets
    used = [False] * 26

    # Loop through each character in the sentence
    for char in sentence:
        # Check if character is an alphabet
        if char.isalpha():
            # Get the index of the alphabet (a=0, b=1, ...)
            index = ord(char) - ord('a')
            # Mark the alphabet as used
            used[index] = True

    # Check if all alphabets are used
    if all(used):
        return "pangram"
    else:
        return "not a pangram"

print(is_pangram())