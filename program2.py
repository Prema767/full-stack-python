
import random

number = random.randint(1, 10)
attempts = 0
score = 100

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Congratulations! Correct guess!")
        print("Attempts:", attempts)
        print("Your score:", score)
        break

    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    score -= 10

print("Game Over!")
