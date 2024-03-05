import os
import random

import getch

from entity import Entity
from event import Event
from map import Map
from tile import Biome

os.system("")


class game:
    def __init__(self, entity: Entity):
        self.entity = entity
        self.event = Event()
        self.game_map = Map(30, 15, entity)
        self.run()

    def run(self) -> None:
        while True:
            os.system("clear")
            self.game_map.display_map()
            print("w: up, a: left, s: down, d: right, q: quit")
            direction = getch.getch()
            if direction == "w" and self.game_map.player.y > 0:
                self.game_map.player.y -= 1
            elif direction == "a" and self.game_map.player.x > 0:
                self.game_map.player.x -= 1
            elif direction == "s" and self.game_map.player.y < self.game_map.height - 1:
                self.game_map.player.y += 1
            elif direction == "d" and self.game_map.player.x < self.game_map.width - 1:
                self.game_map.player.x += 1
            elif direction == "q":
                print("Quitting the game.")
                exit()
            else:
                print("Invalid input. Use W/A/S/D to move or Q to quit.")
                continue
            tile = self.game_map.map_data[self.game_map.player.y][
                self.game_map.player.x
            ]
            tile = self.game_map.map_data[self.game_map.player.y][
                self.game_map.player.x
            ]
            biome = tile.biome
            event_message = biome.generate_event()
            print(event_message)
            # if tile == ".":
            #     wait = input("Press enter to continue.")
            #     self.event.handler(tile)


if __name__ == "__main__":
    entity = Entity("Player", 100, 1, 1)
    gameplay = game(entity)
    gameplay.run()
