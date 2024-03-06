ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_WHITE = "\033[97m"
ANSI_CYAN = "\033[36m"


class Tile:
    def __init__(self, symbol: str, color: str | None = None, biome=None):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if color else symbol
        self.biome = biome


class Biome:
    def __init__(self, symbol: str, color: str):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if color else symbol
        self.color = color
        # self.generate_event()

    def generate_event(self):
        return "You are in a biome."
        # print("You are in a biome.")
        raise NotImplementedError("Subclasses must implement generate_event")


class MountainsBiome(Biome):
    def __init__(self):
        super().__init__("▲", ANSI_WHITE)

    # def generate_event(self):
    #     return "You are in a mountain."
    #


class PlainsBiome(Biome):
    def __init__(self):
        super().__init__("`", ANSI_GREEN)

    # def generate_event(self):
    #     return "You are in a forest."


class ForestBiome(Biome):
    def __init__(self):
        super().__init__("♠", ANSI_GREEN)

    def generate_event(self):
        return "You are in a forest."


class PinesBiome(Biome):
    def __init__(self):
        super().__init__("♣", ANSI_GREEN)

    def generate_event(self):
        return "You are in a pine forest."


class WaterBiome(Biome):
    def __init__(self):
        super().__init__("~", ANSI_CYAN)

    def generate_event(self):
        return "You are near water."
