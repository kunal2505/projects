import time
import threading
import random


def game(comp,p1):
    
    
    if comp==p1:
        return None
    #-----------------------
    elif comp=='s':
        if p1=='w':
            return False
        elif p1=='g':
            return True
    #-----------------------
    elif comp=='w':
        if p1=='g':
            return False
        elif p1=='s':
            return True
    #-----------------------
    elif comp=='g':
        if p1=='w':
            return True
        elif p1=='s':
            return False
 
print("\n                     INTRODUCTION TO GAME                 ") 
print("                           ↓                              ")
intro=("Snake Water Gun is a simple game that is played .The rules require that competing players use one hand to form one of three shapes at an agreed-upon time. The person that plays the strongest “object” is the winner of the game.Here we have Python version of this, computer will play it's turn and will choose any one object from Snake ,water or gun .Water will win from gun , gun will win from snake, snake will win from water.")
print(intro.upper())
print("\n========================================================")

print("\nCOMPUTER'S TURN : Snake(s) Water(w) Gun(g)...: ","\n")

print("========================================================")
print("Wait for a while,Computer playing it's turn....\n")

time.sleep(1)


rn=random.randint(1,3)
if rn==1:
    comp='s'
elif rn==2:
    comp='w'
elif rn==3:
    comp='g'

print("                            : )                            ") 
time.sleep(1)
print("                            : )                            ")
time.sleep(1)
print("                            : )                            ")
time.sleep(1)
print("                            : )                            ")
print("                      - NOW YOUR TURN -                    ")

p1=input("YOUR'S TURN : Snake(s) Water(w) Gun(g) ? ")
a=game(comp,p1)
print("\n========> Compter Played:",comp)
print("\n========> You Played:",p1,"\n")
if a==None:
    print("MATCH TIED....")
if a==True:
    print("Player Wins the Game...")
if a==False:
    print("Opponent Wins....")    