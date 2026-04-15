#this code gievs condtions to a user trying to acces something with age and moeny limits

age = int(input ("How old are you? "))
gold_coins = int(input ( "How many gold coins do you have? " ))

if age >= 18 and gold_coins >= 20:

 print( "You can join the party" )

else:
 print("Go home!")


