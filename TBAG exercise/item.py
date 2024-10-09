
class Item():
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description
        self.can_open = False # to set ability to open doors

    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name
    
    def set_can_open(self, can_open):
        self.can_open = can_open
    
    def get_can_open(self):
        return self.can_open