secret_number = 78
user_input = int(input("enter any number you can think of: "))

while int(user_input) != int(secret_number):
    user_input = int(input("Ooh, You got it wrong try again: "))
    
print("Wow, you got it right, congratulations")