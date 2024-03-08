import os
import random
import string
import time
from random import randint

from biome import PlainsBiome
from utils import *


class Entity:
    def __init__(self) -> None:
        self.name = self.generate_random_name()
        self.maxhealth = 10
        self.health = 10
        self.damage = 1

    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)

    def get_health(self) -> str:
        remaining_health_symbol = f"{ANSI_RED}♥{ANSI_RESET}"
        return f"{remaining_health_symbol * self.health}"

    def generate_random_name(self, length=8) -> str:
        letters = string.ascii_letters
        return "".join(random.choice(letters) for _ in range(length))


class Player(Entity):
    def __init__(self, width: int = 0, height: int = 0) -> None:
        super().__init__()
        self.symbol = "☻"
        self.damage = 4
        self.x = randint(0, width - 1)
        self.y = height - 1
        self.potions = 3
        self.food = 3
        self.stamina = 10
        self.flag = False
        self.fight_status = True

    def get_is_fighting(self) -> bool:
        return self.fight_status

    def set_fight_status(self, status: bool) -> None:
        self.fight_status = status

    def drink_potion(self) -> None:
        if self.potions > 0:
            self.health = self.maxhealth
            self.potions -= 1
        else:
            print("You don't have any potions left.")
            wait_for_enter()

    def generate_loot(self) -> None:
        if random.random() < 0.3:
            if random.random() < 0.5 and self.food < 3:
                self.food += 1
                print("You found some food.")
            elif random.random() < 0.5 and self.potions < 3:
                self.potions += 1
                print("You found a potion.")

    def fight(self, entity: Entity) -> None:
        if self.health <= 0:
            print("Game over.")
            exit()
        if entity.health <= 0:
            self.set_fight_status(False)
            # print(f"{entity.name} has died.")
            return
        self.set_fight_status(True)
        entity.attack(self)
        self.attack(entity)
        if not self.flag:
            print("You have a higher chance to be found in plains.")
            self.flag = True

    def hunt(self, map) -> None:
        if self.food >= 5:
            print("You have enough food.")
            wait_for_enter()
            return
        current_biome = map.map_data[self.y][self.x]

        if isinstance(current_biome, PlainsBiome):
            chance = 0.2
            print("You have lower chance to hunt in plains.")
        else:
            chance = 0.6
        if random.random() < chance:
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

    def display_huntscene(self) -> None:
        hunt_art = """
        You successfully hunted for food.
          /\\_/\\
         ( o.o )
          > ^ <
        """
        print(hunt_art)
