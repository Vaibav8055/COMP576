import random

def guessing_game():

    number_to_guess = random.randint(1, 100)
    max_tries = 7
    guesses = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. You have 7 tries to guess it.")

    while guesses < max_tries:

        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number in", guesses, "guesses.")
            break

    if guesses == max_tries and guess != number_to_guess:
        print("Sorry, you've run out of tries. The number was", number_to_guess)


guessing_game()
