import random


num = random.randint(0, 100)
guessNum = int(input())
while num != guessNum:
    #print(num)
    if num > int(guessNum):
        print('The number is greater than ', guessNum)
    if num < int(guessNum):
        print('The number is lower than ', guessNum)
    guessNum = int(input()) 

print('Your number is', guessNum)
