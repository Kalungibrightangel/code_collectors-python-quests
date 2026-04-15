def ask_for_age():
    age = int(input("How old are you? "))
    return age


def can_they_vote():
    age = ask_for_age()

    if age >= 18:
        print("You are allowed to vote")
    else:
        print("Wait a few more years")

can_they_vote()