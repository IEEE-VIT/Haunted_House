import time
import random


'''
Write a challenge which takes two random integers and asks the user for the answer.
The user must answer the question in 60 secs.
If the user is able to correctly answer within the timelimit score is incremented by 20,
in all other cases the score reduces by 5 points.
Give proper print statements where ever necessary.
'''
def witch_challenge(npc,score):
    print(f"Witch: {npc['dialogue']}")
    print(f"Witch: Excellent! {npc['reward']}")
    
    # Write code here

    return score


'''
Write a challenge which takes a random word from the words list and jumbles it.
The jumbled word should we shown to the user and the user should try and unscramble the word.
If the user is able to unscramble the word then the score must increase by 20.
If wrong answer then reduce 5 points.
Give proper print statements where ever necessary.
'''
def knight_challenge(npc, score):
    print(f"Knight: {npc['dialogue']}")
    print(f"Knight: {npc['reward']}")
    words = ["HARDWORK", "SUNFLOWER", "HAUNTED", "MORGUE"]
    num=(int)(random()*10)%4
    string = words[num]
    temp1= string
    temp=string[5]
    string[5]=string[1]
    string[1]=temp
    print(string)
    print("Enter the cirrect word:\n")
    s=input()
    if(s==temp1):
        score+=20
    else:
        score-=5
    return score



'''
Print the dialougue and reward of the ghost.
Award 20 points for finding the required item.
'''
def ghost_challenge(npc, score):
    #Write your code here
    print(f"Ghost: {npc['dialogue']}")
    print(f"Ghost: {npc['reward']}")
    
    score += 20
    return score



'''
Create a challenge for the sorcerer.
Ask the user the given riddle.
If the user answers the riddle correctly, award them 20 points,
else they loose 5 points.
'''
def sorcerer_challenge(npc, score):
    print(f"Sorcerer: {npc['dialogue']}")

# write your code here

    return score