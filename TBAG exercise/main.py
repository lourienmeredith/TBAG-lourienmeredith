
from room import Room
from character import Enemy
from character import Friend
from item import Item

# instanciate rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

# instanciate character 1
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi I'm Dave and I totally won't eat you")
dave.set_weakness("cheese")
dave.set_treasure("stinky brain")
dave.set_dirty_money(80)
dave.send_to_sleep("melatonin")
dining_hall.set_character(dave)

# instanciate character 2
jerry = Enemy("Jerry", "A greedy rat")
jerry.set_conversation("Hey I'm Jerry and your cheese is safe with me")
jerry.set_weakness("mouse trap")
jerry.set_treasure("blue cheese")
jerry.set_dirty_money(65)
jerry.send_to_sleep("melatonin")
ballroom.set_character(jerry)

# instanciate character 3
miffy = Friend("Miffy", "A cute bunny")
miffy.set_conversation("Hello I'm Miffy and I like to hop around")
miffy.set_treasure("yummy carrots")
kitchen.set_character(miffy)

# instanciate item
key = Item("Key", "A shiny golden tool.")
key.set_can_open(True) # set to have ability to open doors
ballroom.set_item(key) # place in a specific room

# set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")

# link rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# game loop
current_room = kitchen # starts in the kitchen
inventory = [] # start with empty inventory

#want game to continue running as long as it can
while True:
    print("\n") # gives new line
    current_room.get_details() # display room details

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe() # show inhabitant if present
    
    command = input("Enter a command:> ")
    
    # added talk function
    if command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to.")

    # added fight function    
    elif command == "fight":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy): # check if character is an enemy
                fight_with = input("Enter combat item you will fight with:> ")
                if inhabitant.fight(fight_with):
                    current_room.set_character(None) # remove enemy after defeating
                else:
                    break # game loop ends if you lose
            else:
                print(f"{inhabitant.name} doesn't want to fight with you") # if character is not enemy, no fights
        else:
            print("There is no one here to fight.")

    # added steal function  
    elif command == "steal":
        if inhabitant is not None:
            print("What do you want to steal?")
            target = input("Enter the treasure you want: ")
            inhabitant.steal(target)
        else:
            print("There is no one to steal from.")

    # added bribe function
    elif command == "bribe":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                dabloons = input("Enter how much you'd pay for bad service:> ")
                inhabitant.bribe(dabloons)
            else:
                print("Good people don't take dirty money.")
        else:
            "There is no one to bribe."

    # added send to sleep function
    elif command == "sleep":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                potion = input("Enter sleeping potion type:> ")
                inhabitant.send_to_sleep(potion)
        else:
            "There is no one to put to sleep."
    
    # added hug function
    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                inhabitant.hug()
            else:
                print("Enemies don't hug. That's only for sillies!")
        else:
            print("There is no one here to hug.")

    elif command == "gift":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                present_name = input("Enter what you'd like to be gifted:> ")
                inhabitant.offer_gift(present_name)
            else:
                print("Don't ever ask again. The gift of wrath is what enemies give.")
        else:
            print("No one can give you anything here.")
    
    elif command == "collect key":
        if current_room.get_item() is not None:
            inventory.append(current_room.get_item()) # add key to inventory
            print(f"You picked up {current_room.get_item().get_name()}")
            current_room.remove_item() # remove item from the room
        else:
            print("There's no key to pick up.")
    
    elif command == "open door":
        if "Key" in [item.get_name() for item in inventory]:
            print("You opened the door to exit game! BYE!")
            break
        else:
            print("You don't have the key to exit this place.")
    else:
        current_room = current_room.move(command) # move to another room