# Quest 15: Nested Riddle - A Mini Adventure with Nested If Statements
direction = input("Do you go LEFT or RIGHT? (left/right): ").lower()

if direction == "left":
 
    action = input("Do you SWIM across or WAIT for help? (swim/wait): ").lower()
    
    if action == "swim":
        print("\n Success! You swim across and find a hidden treasure chest!")
        print("Quest completed: You are rich!")
    else:
        print("\n You wait too long. Turn back")
        print("Quest failed: No treasure for you.")
        
elif direction == "right":
    print("\nYou go right and encounter a stranger.")
    print("Quest failed: Adventure ended.")
    
else:
    print("\n That's not a valid choice.")
    print("Quest failed: Invalid path.")