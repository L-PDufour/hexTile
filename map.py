from math import e
from random import randint, random

from entity import Entity
from tile import Tile, forest, mountain, pines, plains, water


class Map:
    def __init__(self, width: int, height: int, entity: Entity) -> None:
        self.width = width
        self.height = height

        self.map_data: list[list[Tile]]

        self.player = entity
        # self.player.x = 0
        # self.player.y = self.height - 1
        self.generate_map()
        self.generate_patch(forest, 3, 3, 5)
        self.generate_patch(pines, 3, 3, 5)
        self.generate_patch(mountain, 2, 3, 3)
        self.generate_patch(water, 1, 3, 5)
        self.generate_line(water)
        # self.generate_player(player_symbol)

    def generate_player(self, tile: Tile) -> None:
        if 0 <= self.player.x < self.width and 0 <= self.player.y < self.height:
            self.map_data[self.player.y][self.player.x] = tile

    def generate_line(self, tile: Tile) -> None:
        start_x, start_y = randint(0, self.height - 1), 0

        while start_x != self.width and start_y != self.height:
            self.map_data[start_y][start_x] = tile
            if random() < 0.5:
                start_x += 1
            else:
                start_y += 1

    def generate_map(self) -> None:
        self.map_data = [
            [plains for _ in range(self.width)] for _ in range(self.height)
        ]

    def generate_patch(
        self,
        tile: Tile,
        num_patches: int,
        min_size: int,
        max_size: int,
        irregular: bool = True,
    ) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile

    def clear_player(self) -> None:
        self.map_data[self.player.y][self.player.x] = " "

    def display_map(self) -> None:
        # self.generate_player(player_symbol)
        frame = "x" + self.width * "=" + "x"
        print(frame)
        for y, row in enumerate(self.map_data):
            row_tiles = [tile.symbol for tile in row]
            if y == self.player.y:
                row_tiles[self.player.x] = "P"
            print("|" + "".join(row_tiles) + "|")
        print(frame)

    def get_tile(self, x: int, y: int) -> Tile:
        return self.map_data[y][x]
# def display_map(self) -> None:
#     frame = "x" + self.width * "=" + "x"
#     print(frame)
#
#     for y, row in enumerate(self.map_data):
#         row_tiles = [tile.symbol for tile in row]
#
#         # Display content in the first window (left side)
#         if y == self.player.y:
#             row_tiles[self.player.x] = "P"
#
#         # Concatenate hero's status to the row content
#         hero_status = f"Hero: Health({self.player.health}) Attack({self.player.attack}) Defense({self.player.defense})"
#         combined_row = "|" + "".join(row_tiles) + "|" + hero_status
#
#         print(combined_row)
#
#     print(frame)

