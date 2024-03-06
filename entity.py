import os
import random
import string
import time
from random import randint


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
        remaining_health_symbol = "♥"
        return f"{remaining_health_symbol * self.health}"

    def display_status(self) -> None:
        print(f"Name: {self.name}")
        print(f"HP: {self.display_health()}")
        if isinstance(self, Player):
            print(f"X: {self.x} Y: {self.y}")
            print(f"Potions: {self.display_potions()}")
            print(f"Foods: {self.display_food()}")
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

    def generate_random_name(self, length=8):
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for _ in range(length))

    def fight(self, entity: Entity) -> None:
        os.system("clear")
        while entity.health > 0 and self.health > 0:
            os.system("clear")
            self.attack(entity)
            entity.attack(self)
            self.display_fight_status(entity)
            if self.health <= 0:
                print(f"{entity.name} has died.")
                print("Game over.")
                exit()
            if entity.health <= 0:
                print(f"{entity.name} has died.")
                if random.random() < 0.3 and self.potions < 3:
                    self.potions += 1
                    print("You found a potion.")
            time.sleep(1)

    def display_fight_status(self, entity: Entity) -> None:
        print(f"{self.name} is fighting {entity.name}!")
        print(f"Name: {self.name}")
        print(f"HP: {self.display_health()}")
        print(f"X: {self.x} Y: {self.y}")
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
