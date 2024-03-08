import os

from display import Display
from entity import Player
from game import Game
from input import Input
from map import Map
from utils import wait_for_enter

os.system("")

height = 15
width = 30


def main():
    player = Player(width, height)
    map = Map(width, height, player)
    display = Display(map, player, width, height)
    input = Input(map, display)
    gameplay = Game(player, map, display)
    gameplay.intro()
    display.render_screen()
    input.input_direction()
    while True:
        display.render_screen()
        gameplay.event()
        player.get_status()
        input.input_direction()
    exit()


if __name__ == "__main__":
    main()
