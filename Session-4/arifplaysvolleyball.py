"""Problem Description:
Arif likes to play volley ball. He found some statistics of matches which described who won the points in order. 
A game shall be won by the player first scoring 11 points except in the case when both players have 10 points each, then the game shall be won by the first player subsequently gaining a lead of 2 points. 
Could you please help the Arif find out who the winner was from the given statistics? (It is guaranteed that statistics represent always a valid, finished match.)
Constraints:
1 ≤ T ≤ 1000
1 ≤ length(matchscenario) ≤ 100
Input Format:
The first line of the input contains an integer 'T', denoting the number of test cases. The description of 'T' test cases follows. 
Each test case consist a binary string 'S', which describes a match. 
'0' means Arif lose a point, whereas '1' means he won the point.
Output Format:
Print the output on a separate line a string describing who won the match. 
If Arif won then print "WIN" (without quotes), otherwise print "LOSS" (without quotes).

Logical Test Cases
Test Case 1
INPUT (STDIN)
4
0101111111111
10110101101010
11100101101101
EXPECTED OUTPUT
WIN
LOSS
Test Case 2
INPUT (STDIN)
6
0001111111111
11100000000000
1001111111111
1000110100101
1111001110011
1000100111011
EXPECTED OUTPUT
LOSS
WIN
LOSS"""

# function to determine the winner of a single match
def determine_winner(match):
    arif_score = 0
    opponent_score = 0
    score_set = set() # use a set to keep track of the scores
    for i in range(len(match)):
        if match[i] == '1':
            arif_score += 1
        else:
            opponent_score += 1
        if (arif_score >= 11 or opponent_score >= 11) and abs(arif_score - opponent_score) >= 2:
            if arif_score > opponent_score:
                return "WIN"
            else:
                return "LOSS"
        score_set.add((arif_score, opponent_score)) # add the current score to the set
    # check if the match ended with a score less than 11-10
    last_score = list(score_set)[-1]
    if last_score[0] >= 11 or last_score[1] >= 11:
        if last_score[0] > last_score[1]:
            return "WIN"
        else:
            return "LOSS"
    else:
        return "LOSS"
# main function
if __name__ == "__main__":
    t=int(input()) # number of test cases
    for i in range(t):
        matchscenario=str(input()) # input string describing match
        result = determine_winner(matchscenario)
        print(result) # print the winner of the match