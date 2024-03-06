import os
import random
import string

import getch

from entity import Entity
from event import Event
from map import Map
from tile import Biome, ForestBiome, MountainsBiome, PinesBiome, PlainsBiome, WaterBiome

os.system("")


def input_direction(direction: str, game_map: Map) -> None:
    if direction == "w" and game_map.player.y > 0:
        game_map.player.y -= 1
    elif direction == "a" and game_map.player.x > 0:
        game_map.player.x -= 1
    elif direction == "s" and game_map.player.y < game_map.height - 1:
        game_map.player.y += 1
    elif direction == "d" and game_map.player.x < game_map.width - 1:
        game_map.player.x += 1
    elif direction == "q":
        print("Quitting the game.")
        exit()
    else:
        print("Invalid input. Use W/A/S/D to move or Q to quit.")


def display_health(entity: Entity) -> str:
    remaining_health_symbol = "♥"
    return f"{remaining_health_symbol * entity.health}"


def display_status(entity: Entity) -> None:
    frame_width = 32  # Adjust this value based on your needs
    frame = "O" + "=" * (frame_width - 2) + "O"

    print(frame)
    print(f"| Name: {entity.name:<{frame_width-10}} |")
    print(f"| HP: {display_health(entity):<{frame_width-8}} |")
    print(f"| X: {entity.x} Y: {entity.y:<{frame_width-12}} |")
    print(frame)


def generate_random_name(length=8):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


class game:
    def __init__(self, entity: Entity):
        self.entity = entity
        self.event = Event()
        self.game_map = Map(30, 15, entity)
        self.run()

    def run(self) -> None:
        while True:
            os.system("clear")
            display_status(self.entity)
            self.game_map.display_map()
            print("w: up, a: left, s: down, d: right, q: quit")
            direction = getch.getch()
            input_direction(direction, self.game_map)
            tile = self.game_map.map_data[self.game_map.player.y][
                self.game_map.player.x
            ]
            msg = tile.biome.generate_event()
            print(msg)
            wait = input("Press enter to continue.")
            self.entity.health -= 1


if __name__ == "__main__":
    random_name = generate_random_name()
    entity = Entity(random_name, 10, 1, 1)
    gameplay = game(entity)
    gameplay.run()
