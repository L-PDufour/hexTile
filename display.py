import os
import sys
import time
from random import randint

from biome import *
from entity import Entity, Player
from map import Map

legend = [
    "Biome | Stamina Cost",
    f"{ANSI_GREEN}., {ANSI_RESET} 1",
    f"{ANSI_GREEN}T♣♠¶ {ANSI_RESET} 2",
    f"{ANSI_WHITE}▲{ANSI_RESET} 3",
    f"{ANSI_CYAN}~' {ANSI_RESET} Unwalkable",
    f"{BROWN_COLOR}= {ANSI_RESET} 1",
    f"{ANSI_TOWN_COLOR}⌂ Town{ANSI_RESET}",
]


class Display:
    def __init__(self, game_map: Map, player: Player, width: int, height: int):
        self._player = player
        self._map = game_map
        self._width = width
        self._height = height

    @property
    def player(self):
        return self._player

    @property
    def map(self):
        return self._map

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def display_map(self) -> None:
        frame = "O" + self.width * "=" + "O"
        print(frame)
        for y, row in enumerate(self.map.map_data):
            row_tiles = []
            for biome in row:
                if isinstance(biome, Biome):
                    row_tiles.append(biome.symbol)
            if y == self.player.y:
                while self.map.map_data[self.player.y][self.player.x].walkable == False:
                    self.player.x = randint(0, self.width - 1)
                row_tiles[self.player.x] = self.player.symbol
            legend_entry = legend[y] if y < len(legend) else ""
            print("|" + "".join(row_tiles) + "|" + " " + legend_entry)
        print(frame)
        print("Use W/A/S/D to move or Q to quit")
        print("Use P to drink potions")
        print("Use H to hunt in a forest")

    def render_screen(self):
        os.system("clear")
        self.display_status()
        self.display_map()
        sys.stdout.flush()

    def render_fight_screen(self, entity) -> None:
        while self.player.get_is_fighting():
            self.render_screen()
            self.display_fight_status(entity)
            self.player.fight(entity)
            print("Press Enter to continue...", end="", flush=True)
            input()
        self.render_screen()

    def display_status(self) -> None:
        print(f"Name: {self._player.name}")
        print(f"HP: {self._player.get_health()}")
        print(f"Potions: {self.display_potions()} Foods: {self.display_food()}")
        print(f"Stamina: {self.display_stamina()}")

    def display_fight_status(self, entity: Entity) -> None:
        print(f"{self._player.name} is fighting {entity.name}!\n")
        print(f"Name: {self._player.name}")
        print(f"HP: {self._player.get_health()}")
        print("-------------------")
        print(f"Name: {entity.name}")
        print(f"HP: {entity.get_health()}")

    def display_stamina(self) -> str:
        stamina_symbol = "♨"
        return f"{stamina_symbol * self._player.stamina}"

    def display_food(self) -> str:
        food_symbol = "⚲"
        return f"{food_symbol * self._player.food}"

    def display_potions(self) -> str:
        potion_symbol = "⚱"
        return f"{potion_symbol * self._player.potions}"
