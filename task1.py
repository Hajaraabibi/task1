import random
myName = input("Hi there! What is your name? ")
number = random.randint(1,10)
print("hello again," + myName + " i am thinking of a number... the number is between 1 and ten")
guess = int(input("can you take a guess:"))

if guess == number:
    print("well done," + myName + "!! You guessed the number i was thinking of")
else:
    print("that is not the number i was thinking of, try again next time")
