import random

words=["names","gender","email","country","mobile","university","major","job","religion"]
randomWord=random.choice(words)

name=input("enter your name: ")
char=input("guess any alphabet: ")
trials=1

while trials < 7:
    if char in randomWord:
        print("your guess ", char," is in word ", randomWord)
        break


    else:
        char = input("guess another alphabet: ")
        trials += 1

if trials == 7:
    print("you reached the maximum number of trails")