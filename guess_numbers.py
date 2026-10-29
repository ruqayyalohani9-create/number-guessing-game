import random

def guessing_game():
    number = random.randint(1, 20)

    print("Guess the number between 1 and 20!")

    for attempt in range(2):
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("Correct! You won!")
            return
        else:
            print("Wrong guess! Try again.")

    print("Game Over! The number was", number)

guessing_game()