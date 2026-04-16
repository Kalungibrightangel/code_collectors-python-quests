#nested function, as for age then chekcs if tehy are aold enough


def ask_for_age():
    age = int(input("Enter your age: "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You can vote!")
    else:
        print("You are too young to vote.")


user_age = ask_for_age()
can_they_vote(user_age)