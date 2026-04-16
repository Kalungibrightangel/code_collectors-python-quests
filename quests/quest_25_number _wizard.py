#updating number guessing game (quest 18) by adding if condition inside while loop
secret_number = 78
user_input = int(input("enter any number you can think of: "))

while int(user_input) != int(secret_number):
    if int(user_input) < int(secret_number):
        print("Oaps! Your guess was too low")
    if int(user_input) > int(secret_number):
        print("Your guess is  too high")
    user_input = int(input("try again: "))
    
print("Wow, you got it right, congratulations")