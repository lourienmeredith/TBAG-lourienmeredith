
class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None # to hold an item in a room
    
    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description
    
    def describe(self):
        print(self.description)
    
    def set_name(self, room_name):
        self.name = room_name
    
    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character
    
    def set_item(self, item):
        self.item = item
    
    def get_item(self):
        return self.item
    
    def remove_item(self):
        self.item = None # remove the item when collected
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    
    def get_details(self):
        print(f"You are in the {self.name}")
        print("--------------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self # player linked back to room they were already in