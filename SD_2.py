import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Get the user's guess
    user_guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the user's guess is correct
    if user_guess == secret_number:
        print(f" Congratulations! You guessed the number in {attempts} attempts.")
        break

    # Provide feedback if the guess is too high or too low
    elif user_guess > secret_number:
        print("Your guess is too high. Try again!")
    else:
        print("Your guess is too low. Try again!")

print("Thanks for playing!")
