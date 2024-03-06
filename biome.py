import random

ANSI_RESET = "\033[0m"
ANSI_TOWN_COLOR = "\033[34;1m"  # Bold blue
BROWN_COLOR = "\033[0;33m"  # Adjust ANSI escape codes for brown color as needed

ANSI_YELLOW_SHADES = [
    "\033[33m",  # Light yellow
    "\033[33;1m",  # Bold yellow
    "\033[33;2m",  # Dim yellow
    "\033[33;3m",  # Italic yellow
    # "\033[33;4m",  # Underline yellow
]
ANSI_GREEN_SHADES = [
    "\033[32m",  # Light green
    "\033[33m",  # Light yellow
    "\033[32;1m",  # Bold green
    "\033[32;2m",  # Dim green
    "\033[32;3m",  # Italic green
    "\033[32;4m",  # Underline green
    "\033[32;9m",  # Strikethrough green
    "\033[97m",  # Light white
]
ANSI_WHITE_SHADES = [
    "\033[97m",  # Light white
    "\033[97;1m",  # Bold white
    "\033[97;2m",  # Dim white
    "\033[97;3m",  # Italic white
    "\033[97;4m",  # Underline white
    "\033[97;9m",  # Strikethrough white
]
ANSI_CYAN = "\033[36m"  # Light cyan


class Biome:
    def __init__(self, symbol: str, color: str):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if color else symbol
        self.color = color
        self.walkable = True

    def generate_event(self):
        raise NotImplementedError("Subclasses must implement generate_event")


class MountainsBiome(Biome):

    def __init__(self):
        symbols = "▲"
        self.random_color = random.choice(ANSI_WHITE_SHADES)
        self.stamina_cost = 3
        super().__init__(symbols, self.random_color)

    def generate_event(self):
        print("You are in a moutains.")


class PlainsBiome(Biome):

    def __init__(self):
        symbols = [
            ".",
        ]
        self.random_symbol = random.choice(symbols)
        self.stamina_cost = 1
        super().__init__(self.random_symbol, ANSI_GREEN_SHADES[0])

    def generate_event(self):
        print("You are in a plains.")


class ForestBiome(Biome):

    def __init__(self):
        symbols = ["T", "♣", "♠", "¶"]
        self.random_symbol = random.choice(symbols)
        self.random_color = random.choice(ANSI_GREEN_SHADES)
        self.stamina_cost = 2
        super().__init__(self.random_symbol, self.random_color)

    def generate_event(self):
        print("You are in a forest.")


class WaterBiome(Biome):
    def __init__(self):
        super().__init__("~", ANSI_CYAN)
        self.walkable = False

    def generate_event(self):
        print("You are near water.")


class RiverBiome(Biome):

    def __init__(self):

        self.stamina_cost = 1
        if random.randint(0, 8) == 0:
            super().__init__("=", BROWN_COLOR)
            self.walkable = True
        else:
            super().__init__("'", ANSI_CYAN)
            self.walkable = False

    def generate_event(self):
        print("You are near water.")


class TownBiome(Biome):
    def __init__(self):
        super().__init__("⌂", ANSI_TOWN_COLOR)

    def generate_event(self):
        print("You have won the game.")
        input("Press enter to exit.")
        exit()
