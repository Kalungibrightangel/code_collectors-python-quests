# The secret code the user needs to guess
secret_code = 42

# Counter to track how many attempts the user has made
attempts = 0

# Keep looping as long as the user has not used all 3 attempts
while attempts < 3:

    # Ask the user to enter a guess
    guess = int(input("Enter your guess: "))

    # Increment the attempt counter by 1 each time a guess is made
    attempts += 1

    # Check if the guess is correct
    if guess == secret_code:
        print("Correct! You cracked the code!")
        # Stop the loop immediately since the user guessed correctly
        break

    # If the guess is too low, give a hint
    elif guess < secret_code:
        print("Too low! Try again.")

    # If the guess is too high, give a hint
    else:
        print("Too high! Try again.")

    # Check if the user has used all 3 attempts without guessing correctly
    # If so, reveal the secret code and end the game
    if attempts == 3 and guess != secret_code:
        print("Game over! The secret code was 42.")