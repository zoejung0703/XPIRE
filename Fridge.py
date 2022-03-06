

from datetime import date
from datetime import timedelta

class Fridge:

    def __init__(self, contents):
        contents = {}
        self.contents = contents
    
    def add_item(self, item_name, due, quantity = 1):
        # due should be ('year-month-day')
        if item_name in self.contents.keys():
            if self.contents[item_name]["due"] == date.fromisoformat(due):
                self.contents[item_name]["quantity"] += quantity
            else:
                # item_name = item_name + "1"
                self.contents[item_name + "1"] = {"quantity" : quantity, "due" : due}
        else: 
            self.contents[item_name] = {"quantity" : quantity, "due" : date.fromisoformat(due)}

    def eat(self, item_name, quantity):
        if item_name in self.contents.keys():
            self.contents[item_name]["quantity"] -= quantity
            if self.contents[item_name]["quantity"] <= 0:
                self.contents.pop(item_name)
        else:
            print("{0} was not in the fridge".format(item_name))

    def calculate_due(self, item_name, due):
        d0 = self.contents[item_name]["due"]
        d1 = date.today()
        daysLeft = d0 - d1
        self.contents[item_name]["daysLeft"] = daysLeft
    
    def notification(self):
        DelList = []
        MoreList = []
        print("")
        print("Notifications:")
        print("")
        print("Items due within a week:")
        for item_name in self.contents:
            daysLeft = self.contents[item_name]["daysLeft"]
            if timedelta(days = 0) <= daysLeft <= timedelta(days = 7):
                print("You have {1} days left until expiry for {0} with quantity of {2}.".format(item_name, self.contents[item_name]["daysLeft"].days, self.contents[item_name]["quantity"]))
            elif daysLeft < timedelta(days = 0):
                DelList.append(item_name)
            else:
                MoreList.append(item_name)
        for item_name in DelList:
            print("{0} has exceeded the expiry date.".format(item_name))
            self.contents.pop(item_name)
        print("")
        print("Other items in your fridge:")
        for item_name in MoreList:
            print("You have {1} days left until expiry for {0} with quantity of {2}.".format(item_name, self.contents[item_name]["daysLeft"].days, self.contents[item_name]["quantity"]))

    def eachDay(self):
        for item_name in self.contents:
            self.calculate_due(item_name, self.contents[item_name]["due"])
        self.notification()


fridge1 = Fridge("F1")

"""
Interface
"""

Done = False


while Done == False:
    item_name, due, quantity = input("Please write the item name, due date(YYYY-MM-DD) and the quantity each separated by a space.").split(" ")
    fridge1.add_item(item_name, due, quantity)
    progress = input("Are you done? (yes/no)")
    if progress == "yes":
        Done = True


# fridge1.eat("apple", 1)

fridge1.eachDay()
