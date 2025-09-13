import time
import random

print("Welcome to snake and ladders!")
print()
time.sleep(2)
print("The rules of the game are as follows:")
time.sleep(2)
print("1. Four players can play at a time")
time.sleep(2)
print("2. Press Enter key to roll the dice")
time.sleep(2)
print("3. Be aware of the snakes....they can catch you at: 17, 31, 45, 59, 68, 87, 99.....if they do so...You will come some steps back")
time.sleep(5)
print("4. There are ladders too!!...they are at: 5, 21, 39, 52, 69, 81")
print()

def moves(a):
    enter1=input("Press Enter to roll dice:")
    o=random.randint(1,6)
     
    if enter1=='':
         print("You rolled a", o)
         a+=o
         print("Your current score is:", a)
         if a==17:
             print("Oops!!...a snake caught you!!....You will go 10 steps back")
             a=a-10
         elif a==31:
             print("Oops!!...a snake caught you!!...you will go 5 steps back")
             a=a-5
         elif a==45:
             print("Oops!!...a snake caught you!!...you will go 15 steps back")
             a=a-15
         elif a==59:
             print("Oops!!...a snake caught you!!...you will go 5 steps back")
             a=a-5
         elif a==68:
             print("Oops!!...a snake caught you!!...you will go 7 steps back")
             a=a-7
         elif a==87:
             print("Oops!!...a snake caught you!!...you will go 30 steps back")
             a=a-30
         elif a==99:
             print("Oops!!...a snake caught you!!...you will go 94 steps back")
             a=a-94
         elif a==5:
             print("Congo!!...you got a ladder...you will go 9 steps ahead")
             a=a+9
         elif a==21:
             print("Congo!!...you got a ladder...you will go 15 steps ahead")
             a=a+15
         elif a==39:
             print("Congo!!...you got a ladder...you will go 10 steps ahead")
             a=a+10
         elif a==52:
             print("Congo!!...you got a ladder...you will go 27 steps ahead")
             a=a+27
         elif a==69:
             print("Congo!!...you got a ladder...you will go 16 steps ahead")
             a=a+16
         elif a==81:
             print("Congo!!...you got a ladder...you will go 6 steps ahead")
             a=a+6
             print("Your current score is:", a)
         return a



a=input("Enter the name of player 1:")
b=input("Enter the name of player 2:")
c=input("Enter the name of player 3:")
d=input("Enter the name of player 4:")
e=0
f=0
g=0
h=0
print()

while e<100 and f<100 and g<100 and h<100:
     print(a, "Go:")
     e=moves(e)
     if e>=100:
        break
     print()
      
     print(b , "Go:")     
     f=moves(f)
     if f>=100:
           break
     print()
         
     
     print(c, "Go:")
     g=moves(g)
     if g>=100:
            break
     print()
        
     print(d, "Go:")
     h=moves(h)
     if h>=100:
           break
     print()
print()     
if e>=100:
    print(a, "Won!!")
elif f>=100:
    print(b, "Won!!")
elif g>=100:
    print(c, "Won!!")
else:
    print(d, "Won!!")
