import os
import random
import string
import time
from random import randint

from utils import wait_for_enter

ANSI_RED = "\033[31m"
ANSI_RESET = "\033[0m"

class Entity:
    def __init__(self, name: str, health: int, damage: int = 1) -> None:
        self.name = name
        self.maxhealth = health
        self.health = health
        self.damage = damage

    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)

    def display_health(self) -> str:
        remaining_health_symbol = f"{ANSI_RED}♥{ANSI_RESET}"
        return f"{remaining_health_symbol * self.health}"

    def display_status(self) -> None:
        print("\n")
        print(f"Name: {self.name}")
        print(f"HP: {self.display_health()}")
        if isinstance(self, Player):
            print(f"Potions: {self.display_potions()} Foods: {self.display_food()}")
            print(f"Stamina: {self.display_stamina()}")


class Player(Entity):
    def __init__(
        self, name: str, health: int, damage: int = 5, width: int = 0, height: int = 0
    ) -> None:
        super().__init__(name, health, damage)
        self.generate_random_name()
        self.symbol = "☻"
        self.x = randint(0, width - 1)
        self.y = height - 1
        self.potions = 3
        self.food = 3
        self.stamina = 10

    def drink_potion(self) -> None:
        if self.potions > 0:
            self.health = self.maxhealth
            self.potions -= 1
        else:
            print("You don't have any potions left.")
            wait_for_enter()

    def generate_random_name(self, length=8):
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for _ in range(length))

    def generate_loot(self) -> None:
            if random.random() < 0.3:
                if random.random() < 0.5 and self.food < 3:
                    self.food += 1
                    print("You found some food.")
                elif random.random() < 0.5 and self.potions < 3:
                    self.potions += 1
                    print("You found a potion.")

    def fight(self, entity: Entity, game) -> None:
        while entity.health > 0 and self.health > 0:
            os.system("clear")
            game.render_screen()
            self.display_fight_status(entity)
            self.attack(entity)
            entity.attack(self)
            if self.health <= 0:
                print(f"{self.name} has died.")
                print("Game over.")
                exit()
            if entity.health <= 0:
                print(f"{entity.name} has died.")
                self.generate_loot()
            wait_for_enter()
    
    def hunt(self) -> None:
        os.system("clear")
        if random.random() < 0.5:
            self.display_huntscene()
            self.food += 2
            wait_for_enter()
        else:
            self.stamina -= 2
            print("You didn't find any animals.")
            wait_for_enter()

    def get_status(self) -> None:
        if self.health <= 0:
            print("You have died.")
            print("Game over.")
            exit()
        if self.food <= 0:
            print("You have run out of food.")
            print("Game over.")
            exit()
        if self.stamina <= 0:
            print("You need to sleep.")
            self.food -= 1
            self.stamina = 10
            wait_for_enter()

    def display_fight_status(self, entity: Entity) -> None:
        print("\n")
        print(f"{self.name} is fighting {entity.name}!\n")
        print(f"Name: {self.name}")
        print(f"HP: {self.display_health()}")
        print("-------------------")
        print(f"Name: {entity.name}")
        print(f"HP: {entity.display_health()}")

    def display_stamina(self) -> str:
        stamina_symbol = "♨"
        return f"{stamina_symbol * self.stamina}"

    def display_food(self) -> str:
        food_symbol = "⚲"
        return f"{food_symbol * self.food}"

    def display_potions(self) -> str:
        potion_symbol = "⚱"
        return f"{potion_symbol * self.potions}"

    def display_huntscene(self) -> None:
        hunt_art = """
        /\\_ _
        ( o.o )
         > ^ <
        """
        print(hunt_art)
