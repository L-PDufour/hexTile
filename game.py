import os
import random

import getch

from entity import Entity, Player
from map import Map
from utils import print_and_wait


class Game:
    def __init__(self):
        self.player = Player("Player", 10, 5, 30, 15)
        self.game_map = Map(30, 15, self.player)
        self.intro()
        self.run()

    def run(self) -> None:
        while True:
            self.render_screen()
            self.game_map.map_data[self.game_map.player.y][
                self.game_map.player.x
            ].generate_event()
            self.input_direction()
            if random.random() < 0.3:
                enemy = Entity("Enemy", 10, 1)
                self.player.fight(enemy, self)
            self.player.get_status()

    def intro(self) -> None:
        os.system("clear")
        frame_width = 50
        frame = "+" + "=" * (frame_width) + "+"

        print(frame)
        print(
            f"| {'Welcome to hexTile(forget about the hex) Game!':^{frame_width-2}} |"
        )
        print(f"| {'Your goal is to reach the town ⌂.':^{frame_width-2}} |")
        print(f"| {'You have options:':^{frame_width-2}} |")
        print(f"| {'1. Drink potions for health.':^{frame_width-2}} |")
        print(f"| {'2. Hunt for food.':^{frame_width-2}} |")
        print(f"| {'3. Manage your resources wisely.':^{frame_width-2}} |")
        print(f"| {'Running out of health or food leads to death.':^{frame_width-2}} |")
        print(f"| {'Running out of stamina means you cannot move.':^{frame_width-2}} |")
        print(f"| {'Every move costs stamina.':^{frame_width-2}} |")
        print(f"| {'Good luck on your adventure!':^{frame_width-2}} |")
        print(frame)

        player_name = input("Enter your hero name: ")
        print(f"Hello, {player_name}! Press enter to start.")
        input()

    def render_screen(self):
        os.system("clear")
        self.player.display_status()
        self.game_map.display_map()

    def input_direction(self) -> None:
        direction = getch.getch()
        while direction in {"p", "h"}:
            if direction == "p":
                self.game_map.player.drink_potion()
                self.render_screen()
            elif direction == "h":
                self.game_map.player.hunt()
                self.render_screen()
            direction = getch.getch()
        while direction not in {"w", "a", "s", "d", "q"}:
            print_and_wait(
                "Invalid input. Use W/A/S/D to move, P to drink potions, H to hunt, or Q to quit."
            )
            direction = getch.getch()

        current_biome = self.game_map.map_data[self.game_map.player.y][
            self.game_map.player.x
        ]
        new_x, new_y = self.game_map.player.x, self.game_map.player.y

        if direction == "w" and self.game_map.player.y > 0:
            new_y -= 1
        elif direction == "a" and self.game_map.player.x > 0:
            new_x -= 1
        elif direction == "s" and self.game_map.player.y < self.game_map.height - 1:
            new_y += 1
        elif direction == "d" and self.game_map.player.x < self.game_map.width - 1:
            new_x += 1
        elif direction == "q":
            print("Quitting the game.")
            exit()
        if self.game_map.map_data[new_y][new_x].walkable:
            self.game_map.player.x, self.game_map.player.y = new_x, new_y
            self.game_map.player.stamina -= current_biome.stamina_cost
        else:
            print_and_wait("You can't move there.")
