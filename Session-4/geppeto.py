"""Question description
A long time ago, there resided a person called Geppetto. He was old and lived by himself. He had no family of his own. Geppetto was a carpenter. He loved to create stuffs from wood. One day, he thought to make a puppet out of wood. He said, “I will make a little boy and will call him ‘Pinocchio.’ First, Geppetto made some wooden legs and arms. After that, he made the body, and he included hands and feet. Finally, he made a little boy’s head. Geppetto made Pinocchio’s eyes, mouth, and nose. After that, he made his ears. Geppetto worked through out day and night on his wooden puppet. He said to himself, “I wish Pinocchio were a real boy.” A fairy heard Geppetto’s wish. She decided to grant his wish and make the wooden puppet come to life. She said to Pinocchio, “You must promise to be a good and honest boy.” The next day, Geppetto was very happy to hear Pinocchio talk. He loved his wooden son very much. Geppetto smiled. “Now you can go to school with all the other little boys!”. At school, English teacher gave the task to Pinocchio that find the number of vowels in the given set of strings. Can you help Pinocchio to find the number of vowels in the given set of strings. 
Constraints
1≤t≤5
Input Format:
Refer the Test cases
Output Format:
Refer the Test cases

Logical Test Cases
Test Case 1
INPUT (STDIN)
3
invertible
inverse
reverse
EXPECTED OUTPUT
4
3
Test Case 2
INPUT (STDIN)
4
Geppetto
Fairy
Pinocchio
Teacher
EXPECTED OUTPUT
3
2
4
3"""

# Reading the number of test cases
t = int(input())
# Looping through each test case
for i in range(t):
    # Reading the input string
    str1=str(input())
    # Initializing the vowel count
    count = 0
    # Looping through each character in the string
    for j in range(len(str1)):
        # Checking if the character is a vowel
        if str1[j] in "aeiouAEIOU":
            count += 1
    # Printing the vowel count for the current string
    print(count)