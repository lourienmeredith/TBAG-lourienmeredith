# this file is to test functionality of specific methods associated with Character class
# interrupting much of game play loop, just for the sake of testing 

from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()

dave.set_conversation("Hello there! I am going to join your OOP game very soon")

dave.talk()
dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with)