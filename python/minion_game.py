""" 
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.
"""
def minion_game(string):
    p1_score = 0
    p1_name = 'Kevin'
    p2_score = 0
    p2_name='Stuart'
    str_length = len(string)

    for i in range(str_length):
        if string[i] in 'AEIOU':
            p1_score += (str_length - i)
        else:
            p2_score += (str_length - i)
    if p1_score > p2_score:
        print(p1_name , p1_score)
    elif p1_score < p2_score:
        print(p2_name, p2_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)