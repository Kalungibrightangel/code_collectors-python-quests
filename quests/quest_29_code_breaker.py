secret_code = 42
attempts = 0

while attempts < 3:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_code:
        print("Correct! You cracked the code!")
        break
    elif guess < secret_code:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if attempts == 3 and guess != secret_code:
        print("Game over! The secret code was 42.")