
class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True
    
    def set_treasure(self, item_treasure):
        self.treasure = item_treasure
    
    def get_treasure(self):
        return self.treasure
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.treasure = None
        self.dirty_money = None
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}!!")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer! GAME OVER!")
            return False

    def steal(self, target):
        if target.lower() == self.treasure:
            print(f"You stole {target} from {self.name}. Who's really the enemy?")
        else:
            print(f"{self.name} doesn't even own that!")
    
    def set_dirty_money(self, min_amount):
        self.dirty_money = min_amount
    
    def get_dirty_money(self):
        return self.dirty_money
    
    def bribe(self, dabloons):
        if int(dabloons) >= self.dirty_money:
            print(f"{self.name} accepts. Now go away.")
        else:
            print(f"{dabloons} dabloons is not enough, silly goose!")
    
    def send_to_sleep(self, potion):
        if potion.lower() == "melatonin":
            print(f"Good night to {self.name} zzz")
        else:
            print(f"{self.name} is WIDE AWAKE!")

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.treasure = None

    def hug(self):
        print(f"{self.name} is filled with love!")
    
    def offer_gift(self, present_name):
        print(f"{self.name} graciously bestows {present_name} for you")