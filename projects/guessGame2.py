import random
number = random.randint(1,10)

name = input('Hi, Whats your name? ')
print ("Well", name, "I have a number in mind between 1 and 10, take a guess")

guess1 = int(input()) # convert input from string to integer

while guess1 != number:
    if guess1 > number:
        print ('your guess is too high. Try again.')
    elif guess1 < number:
        print ('your guess is too low. Try again.')

    guess1 = int(input()) # asks user to take another guess

print("excellent!")