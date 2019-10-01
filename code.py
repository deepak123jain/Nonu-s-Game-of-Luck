
import random

import time

name=input("Welcome Buddy!! Enter Your Name \n")
num=random.randint(1,200)
print("Hi",name)
print("Instructions--")
print("You have 10 chances to guess the number")
print("You can enter any number between 1 and 500")
print("You will get hints after your first attempt")
print("You will be provided with message whenever you will cross the upper limit")
print("Game Starts in 3 sec")
r=[]
print("!!!!!!!!!!!Please Wait!!!!!!!!!")
time.sleep(3)

print("Start entering the Numbers ")
p=0
while p<10:
    try:
        l=int(input())
    except:
        print("Please Enter A Numeric Value")
        continue
    if l<=0 or l>200:
        print("Please Enter the Number in the range specified")
        continue
    p+=1
    if l==num:
        print("Numbers Matched")
        print("Hurray!! You Won")
        break 
    else:
        if p==1:
            r.append(l)
            print("Sry!! Try Again")
            f=l
        else:
            if l in r:
                print("Sry !! Try Again")
                print("Don't waste your moves by repeating the numbers")
            if l>num:
                print("Stay Trying!! You have crossed the number")
                
            elif abs(l-num)>abs(f-num):
                r.append(l)
                print("Hint!!!! You are away from the number as of last time")
            else:
                r.append(l)
                print("Stay Trying!! You are close to win")
            f=l

else:
    print("You lose!!! Restart the game and try again")
    print("The number was - ",num)
    
    
    
    
