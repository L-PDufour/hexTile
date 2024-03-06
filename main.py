import os
import random
from random import randint

import getch

from entity import Entity, Player
from map import Map

os.system("")


def input_direction(direction: str, game_map: Map) -> None:
    current_biome = game_map.map_data[game_map.player.y][game_map.player.x]

    if direction == "p":
        game_map.player.drink_potion()
        game_map.player.display_status()
    elif direction in {"w", "a", "s", "d"}:
        new_x, new_y = game_map.player.x, game_map.player.y

        if direction == "w" and game_map.player.y > 0:
            new_y -= 1
        elif direction == "a" and game_map.player.x > 0:
            new_x -= 1
        elif direction == "s" and game_map.player.y < game_map.height - 1:
            new_y += 1
        elif direction == "d" and game_map.player.x < game_map.width - 1:
            new_x += 1
        if game_map.player.stamina < 2: 
            print("You don't have enough stamina to move.")
            wait = input("Press enter to sleep.")
            game_map.player.stamina = 10
            game_map.player.food -= 1
        if game_map.map_data[new_y][new_x].walkable:
            game_map.player.x, game_map.player.y = new_x, new_y
            game_map.player.stamina -= current_biome.stamina_cost
      
        else:
            print("You can't move there. The terrain is not walkable.")
            wait = input("Press enter to continue.")
    elif direction == "q":
        print("Quitting the game.")
        exit()
    else:
        print("Invalid input. Use W/A/S/D to move, P to drink potions, or Q to quit.")

class game:
    def __init__(self):
        self.player = Player("Player", 10, 5, 30, 15)
        self.game_map = Map(30, 15, self.player)
        # start_x = randint(0, self.game_map.width - 1)
        # start_y = self.game_map.height - 1
        # self.player.x = start_x
        # self.player.y = start_y
        self.intro()
        self.run()

    def run(self) -> None:
        while True:
            os.system("clear")
            self.player.display_status()
            self.game_map.display_map()
            print("Use W/A/S/D to move or Q to quit")
            print("Use P to drink potions")
            biome = self.game_map.map_data[self.game_map.player.y][
                self.game_map.player.x
            ]
            biome.generate_event()
            direction = getch.getch()
            input_direction(direction, self.game_map)
            if random.random() < 0.3:
                enemy = Entity("Enemy", 10, 1)
                self.player.fight(enemy)

    def intro(self) -> None:
        os.system("clear")
        frame_width = 50
        frame = "+" + "=" * (frame_width) + "+"

        print(frame)
        print(
            f"| {'Welcome to the first AAAAA game in a terminal.':^{frame_width-2}} |"
        )
        print(f"| {'You must find the town.':^{frame_width-2}} |")
        print(f"| {'Good luck.':^{frame_width-2}} |")
        print(f"| {'Choose your hero name carefully.':^{frame_width-2}} |")
        print(f"| {'Because I will not use it.':^{frame_width-2}} |")
        print(frame)

        player_name = input("Enter your hero name: ")
        print(f"Hello, {player_name}! Press enter to start.")
        input()


if __name__ == "__main__":
    gameplay = game()
    gameplay.run()
