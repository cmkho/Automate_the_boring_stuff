#Random Number Guessing Game

import random

print("Welcome to Calvin's guess a number game")
print("First, please enter your name")

username = input()

A = random.randint(1,49)
B = A + 20
secretNumber = random.randint(A,B)

print("Well " + username + ", I am thinking of a whole number between " + str(A) + " and " + str(B) + ".")
print("Try guess the number within 6 guesses")

for guessesTaken in range(1,7):
    guess = input()
    if int(guess) > B or int(guess) < A:
        print("That isn't even in my range dummy!")
    else:      
        try:
            if int(guess) > secretNumber:
                print(str(guess) + " is too high")
            elif int(guess) < secretNumber:
                print(str(guess) + " is too low")
            else:
                break
        except ValueError:
            print("Use numerical numbers for your guessing inputs please")

if int(guess) == secretNumber:
    print("Congratulations! You guessed it in " + str(guessesTaken) + " guesses!")

else:
    print("You fail. The number was " + str(secretNumber) + ".")

