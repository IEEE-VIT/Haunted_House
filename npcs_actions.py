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

    # Write code here

    return score



'''
Print the dialougue and reward of the ghost.
Award 20 points for finding the required item.
'''
def ghost_challenge(npc, score):
    print("Hello i am the GHOST . Help me find my lost locket, and I'll reveal a secret")
    print("if you help me find my lost locket il reward you with 20 points")
    found=input("have you found the lost locket ?? ")
    if found=="yes":
        print("You found the ghost's locket now let me tell ")

    

    return score



'''
Create a challenge for the sorcerer.
Ask the user the given riddle.
If the user answers the riddle correctly, award them 20 points,
else they loose 5 points.
'''
def sorcerer_challenge(npc, score):
    
    print(f"Sorcerer: {npc['dialogue']}")
    score=0
    print("What has keys but can't open locks?")
    ans =input("enter the answer for the riddle : ")
    if ans=="piano":
        print("your answer for the riddle is correct !")
        score=score+20
    else:
        print("Ouch your answer for the riddle is wrong !")
        score=score-5

    return score