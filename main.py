import os
import random

from entity import Entity
from map import Map

os.system("")


class game:
    def __init__(self, entity: Entity):
        self.entity = entity
        self.game_map = Map(30, 15, entity)
        self.run()

    def run(self) -> None:
        while True:
            os.system("clear")
            self.game_map.display_map()
            direction = input("Move (W/A/S/D): ").upper()

            # self.game_map.clear_player()  # Clear the previous player position

            if direction == "W" and self.game_map.player.y > 0:
                self.game_map.player.y -= 1
            elif direction == "A" and self.game_map.player.x > 0:
                self.game_map.player.x -= 1
            elif direction == "S" and self.game_map.player.y < self.game_map.height - 1:
                self.game_map.player.y += 1
            elif direction == "D" and self.game_map.player.x < self.game_map.width - 1:
                self.game_map.player.x += 1
            elif direction == "Q":
                print("Quitting the game.")
                break
            else:
                print("Invalid input. Use W/A/S/D to move or Q to quit.")
                continue
            if random.random() <= 0.5:
                self.game_map.display_event("You found a treasure chest!")
                wait = input("Press enter to continue.")


if __name__ == "__main__":
    entity = Entity("Player", 100, 1, 1)
    gameplay = game(entity)
    gameplay.run()
