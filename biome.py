import random

from utils import *


class Biome:
    def __init__(self, symbol: str, color: str, stamina_cost: int = 1):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if color else symbol
        self.color = color
        self.stamina_cost = stamina_cost
        self.hunted = False
        self.walkable = True

    def generate_event(self):
        raise NotImplementedError("Subclasses must implement generate_event")


class MountainsBiome(Biome):
    def __init__(self):
        symbols = "▲"
        random_color = random.choice(ANSI_WHITE_SHADES)
        super().__init__(symbols, random_color, stamina_cost=3)

    def generate_event(self):
        print("You are in the mountains.")


class PlainsBiome(Biome):
    def __init__(self):
        symbols = [
            ".",
            ",",
        ]
        random_symbol = random.choice(symbols)
        super().__init__(random_symbol, ANSI_GREEN_SHADES[0], stamina_cost=1)

    def generate_event(self):
        print("You are in a plains.")


class ForestBiome(Biome):
    def __init__(self):
        symbols = ["T", "♣", "♠", "¶"]
        random_symbol = random.choice(symbols)
        random_color = random.choice(ANSI_GREEN_SHADES)
        super().__init__(random_symbol, random_color, stamina_cost=2)

    def generate_event(self):
        print("You are in a forest.")


class WaterBiome(Biome):
    def __init__(self):
        super().__init__("~", ANSI_CYAN, stamina_cost=1)
        self.walkable = False

    def generate_event(self):
        print("You are near water.")


class RiverBiome(Biome):
    def __init__(self, map_data, x, y):
        if random.randint(0, 8) == 0 and self.is_adjacent_water_or_river(map_data, x, y):
            super().__init__("=", BROWN_COLOR, stamina_cost=1)
            self.walkable = True
        else:
            super().__init__("'", ANSI_CYAN, stamina_cost=1)
            self.walkable = False

    def is_adjacent_water_or_river(self, map_data, x, y) -> bool:
        if y == 0 or y == len(map_data) - 1 or x == 0 or x == len(map_data[0]) - 1:
            return False

        right_biome = map_data[y][x + 1]
        left_biome = map_data[y][x - 1]

        if isinstance(right_biome, (WaterBiome, RiverBiome)):
            return False
        if isinstance(left_biome, (WaterBiome, RiverBiome)):
            return False
        return True

    def generate_event(self):
        print("You are near water.")


class TownBiome(Biome):
    def __init__(self):
        super().__init__("⌂", ANSI_TOWN_COLOR)

    def generate_event(self):
        print("You have won the game.")
        input("Press enter to exit.")
        exit()

