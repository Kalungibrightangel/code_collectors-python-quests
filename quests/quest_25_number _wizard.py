secret_number = 78
user_input = int(input("enter any number you can think of: "))

while int(user_input) != int(secret_number):
    if int(user_input) < int(secret_number):
        print("Oops! your guess was too low")
    if int(user_input) > int(secret_number):
        print("Bingo! your guess was too high")
    user_input = int(input("Ooh, You got it wrong try again: "))
    
print("Wow, you got it right, congratulations")