import getch

from display import Display
from map import Map
from utils import print_and_wait


class Input:
    def __init__(self, game_map: Map, display: Display) -> None:
        self._game_map = game_map
        self._display = display

    @property
    def game_map(self):
        return self._game_map

    @property
    def display(self):
        return self._display

    def input_direction(self) -> None:
        print("waiting for input...")

        direction_mapping = {
            "w": (-1, 0),  # Move up
            "a": (0, -1),  # Move left
            "s": (1, 0),  # Move down
            "d": (0, 1),  # Move right
            "h": None,  # Hunt (handled separately)
            "p": None,  # Drink potion (handled separately)
            "q": None,  # Quit (handled separately)
        }

        direction = getch.getch()
        while direction not in direction_mapping:
            print_and_wait(
                "Invalid input. Use W/A/S/D to move, P to drink potions, H to hunt, or Q to quit."
            )
            direction = getch.getch()

        if direction == "q":
            print_and_wait("Goodbye!")
            exit()

        if direction == "p":
            self.game_map.player.drink_potion()
            self._display.render_screen()
            self.input_direction()

        elif direction == "h":
            self.handle_hunt()
        else:
            self.handle_movement(direction_mapping[direction])

    def handle_hunt(self) -> None:
        if self.game_map.map_data[self.game_map.player.y][
            self.game_map.player.x
        ].hunted:
            print_and_wait("You have already hunted here.")
            return
        self.game_map.player.hunt(self.game_map)
        self.game_map.map_data[self.game_map.player.y][
            self.game_map.player.x
        ].hunted = True

    def handle_movement(self, movement: tuple[int, int]) -> None:
        new_y, new_x = (
            self.game_map.player.y + movement[0],
            self.game_map.player.x + movement[1],
        )

        if 0 <= new_y < self.game_map.height and 0 <= new_x < self.game_map.width:
            current_biome = self.game_map.map_data[self.game_map.player.y][
                self.game_map.player.x
            ]

            if self.game_map.map_data[new_y][new_x].walkable:
                self.game_map.player.x, self.game_map.player.y = new_x, new_y
                self.game_map.player.stamina -= current_biome.stamina_cost
            else:
                print_and_wait("You can't move there.")
        else:
            print_and_wait("Invalid movement.")
