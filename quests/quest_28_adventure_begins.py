
#this code is an adventure experience with options and two different endings 
def start():
    print("You are appear in a matrix. Two paths appear.")
    print("1. Go left to a party")
    print("2. Go right to a class")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        party()
    elif choice == "2":
        library()
    else:
        print("Invalid choice.")
        start()


def party():
    print("You arrive at the party")
    print("You drink soda")
    print("you get a mystery box from Angel")

    choice = input("Open it? (yes/no): ")

    if choice == "yes":
        ending_death()
    else:
        ending_safe()


def library():
    print("You were lied to")
    print("this is not a class, it is a path to heaven")

    choice = input("Use bridge or boat? (bridge/boat): ")

    if choice == "boat":
        ending_safe()
    else:
        ending_death()

def ending_death():
    print("you wish it was money but it is not, it is a poisonous gas")
    print ("you die because it is real")

def ending_safe():
    print("Safe Return")
    print("You return to your sense because it is a dream")

start()