ANSI_RESET = "\033[0m"
ANSI_TOWN_COLOR = "\033[34;1m"  # Bold blue
BROWN_COLOR = "\033[0;33m"  # Adjust ANSI escape codes for brown color as needed
ANSI_RED = "\033[31m"
ANSI_RESET = "\033[0m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_WHITE = "\033[97m"
ANSI_CYAN = "\033[36m"
ANSI_TOWN_COLOR = "\033[34;1m"  # Bold blue
BROWN_COLOR = "\033[0;33m"
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


def wait_for_enter() -> None:
    input("Press enter to continue.")


def print_and_wait(message: str) -> None:
    print(message)
    wait_for_enter()
