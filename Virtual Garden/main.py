class Plant:
    def __init__(self, name, harvest_yield):
        self.name = name
        self.harvest_yield = harvest_yield
        self.growth_stages = ["seed", "sprout", "mature", "flower", "fruit", "harvest_ready"]
        self.current_stage = self.growth_stages[0]
        self.harvestable = False

    def grow(self):
        current_index = self.growth_stages.index(self.current_stage)

        if current_index < (len(self.growth_stages) - 1):
            self.current_stage = self.growth_stages[current_index + 1]
            if self.current_stage == self.growth_stages[-1]:
                self.harvestable = True

        elif self.current_stage == self.growth_stages[-1]:
            print(f"{self.name} is already fully grown")

    def harvest(self):
        if self.harvestable:
            self.harvestable = False
            return self.harvest_yield
        else:
            return None




""""_____________________________________________________________"""


class Tomato(Plant):
    def __init__(self):
        super().__init__("Tomato", 10)


class Potato(Plant):
    def __init__(self):
        super().__init__("Potato", 3)
        self.growth_stages = ["seed", "sprout", "mature", "harvest_ready"]


class Carrot(Plant):
    def __init__(self):
        super().__init__("Carrot", 5)
        self.growth_stages = ["seed", "sprout", "mature", "harvest_ready"]


""""_____________________________________________________________"""


def select_item(items):  # here items will replace with an inventory dictionary
    if type(items) == dict:
        item_list = list(items.keys())  # "tomato", "potato"
    elif type(items) == list:
        item_list = items  # Tomato(), Potato()

    for i in range(len(item_list)):
        try:
            item_name = item_list[i].name
        except:
            item_name = item_list[i]
        print(f"{i + 1}. {item_name}")

    print()
    while True:
        user_input = input("Select an item ")
        try:
            user_input = int(user_input)
            if 0 < user_input <= len(item_list):
                return item_list[user_input - 1]
            else:
                print("Invalid Input")
        except:
            print("Invalid Input")



"""_______________________________"""

import random


class Gardener:
    """Represent a gardner who can plant and harvest plants."""

    plant_dict = {"Tomato": Tomato, "Potato": Potato, "Carrot": Carrot}

    def __init__(self, name):
        self.name = name
        self.inventory = {}  # seed & harvest yield
        self.planted_plants = []
        self.seeds = ["Potato", "Tomato", "Carrot"]

    def get_seed(self):
        seed = random.choice(self.seeds)

        if seed not in self.inventory:
            self.inventory[seed] = 1
        else:
            self.inventory[seed] += 1

        print(f"{self.name} has found the {seed} seed!")

    def plant(self):
        selected_plant = select_item(self.inventory)  # name

        if selected_plant in self.inventory and self.inventory[selected_plant] > 0:
            self.inventory[selected_plant] -= 1
            if self.inventory[selected_plant] == 0:
                del self.inventory[selected_plant]
            new_plant = self.plant_dict[selected_plant]()

            self.planted_plants.append(new_plant)
            print(f"{self.name} has planted a {selected_plant} plant!")

        else:
            print(f"{self.name} does not have any {selected_plant} plant!")

    def tend(self):
        for plant in self.planted_plants:
            if not plant.harvestable == True:
                plant.grow()
                print(f"{plant.name} is now on a {plant.current_stage} stage!")
            else:
                print(f"{plant.name} is ready to be harvested")

    def harvest(self):
        selected_plant = select_item(self.planted_plants)  # instances
        if selected_plant.harvestable == True:
            if selected_plant.name not in self.inventory:
                self.inventory[selected_plant.name] = selected_plant.harvest()
            else:
                self.inventory[selected_plant.name] += selected_plant.harvest()
            print(f"You have harvested {selected_plant.name}!")
            self.planted_plants.remove(selected_plant)

        else:
            print(f"You can't harvest {selected_plant.name}!")


""""_____________________________________"""

valid_commands = ["help", "seed","plant","tend", "harvest", "quit"]

print("***Welcome to the Virtual Garden***")
print()
gardener_name = input("What is the Gardener Name: ")

gardener = Gardener(gardener_name)
print()

print(f"***Welcome Mr/Mrs {gardener_name} in the Beautiful Virtual Garden***")
print("Type 'help' for valid command. ")
while True:
    print()
    gardener_action = input("What do you want to do? ").lower()
    if gardener_action in valid_commands:
        if gardener_action == "help":
            print("***Available Commands!***")
            for command in valid_commands:
                print(command)
        elif gardener_action == "seed":
            gardener.get_seed()
        elif gardener_action == "plant":
            gardener.plant()
        elif gardener_action == "tend":
            gardener.tend()
        elif gardener_action == "harvest":
            gardener.harvest()
        elif gardener_action == "inventory":
            gardener.inventory()
        elif gardener_action == "quit":
            print("Thank You for coming Virtual Garden")
            break
    else:
        print()
        print("You entered invalid command, please enter correct command!")
        print("Thank You for coming Virtual Garden")