ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"


class Tile:
    def __init__(self, symbol: str, color: str | None = None):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if color else symbol


plains = Tile(".", ANSI_YELLOW)
forest = Tile("󰹩", ANSI_GREEN)
pines = Tile("", ANSI_GREEN)
mountain = Tile("", ANSI_WHITE)
water = Tile("~", ANSI_CYAN)
