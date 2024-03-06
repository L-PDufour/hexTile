import random
# from math import randint
from random import randint

ANSI_YELLOW = "\033[33m"
from entity import Entity
from tile import (Biome, ForestBiome, MountainsBiome, PinesBiome, PlainsBiome,
                  Tile, WaterBiome)


class Map:
    def __init__(self, width: int, height: int, entity: Entity) -> None:
        self.width = width
        self.height = height
        self.map_data = []
        self.player = entity

        self.generate_map()
        self.generate_patch(ForestBiome(), 5, 4, 7)
        self.generate_patch(PinesBiome(), 5, 4, 7)
        self.generate_patch(MountainsBiome(), 3, 3, 5)
        self.generate_patch(WaterBiome(), 2, 3, 5)
        self.generate_line(WaterBiome())

    def generate_map(self) -> None:
        self.map_data = [
            [Tile(".", ANSI_YELLOW, PlainsBiome()) for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def display_map(self) -> None:
        frame = "O" + self.width * "=" + "O"
        print(frame)
        for y, row in enumerate(self.map_data):
            row_tiles = [biome.symbol for biome in row]
            if y == self.player.y:
                row_tiles[self.player.x] = self.player.symbol
            print("|" + "".join(row_tiles) + "|")
        print(frame)

    def generate_line(self, biome: Biome) -> None:
        start_x, start_y = randint(0, self.height - 1), 0
        tile = Tile(biome.symbol, biome.color, biome)

        while start_x != self.width and start_y != self.height:
            self.map_data[start_y][start_x] = tile
            if random.random() < 0.5:
                start_x += 1
            else:
                start_y += 1

    def generate_patch(
        self,
        biome: Biome,
        num_patches: int,
        min_size: int,
        max_size: int,
        irregular: bool = True,
    ) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(0, self.width - width)
            start_y = randint(0, self.height - height )

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    tile = Tile(biome.symbol, biome.color, biome)
                    self.map_data[start_y + i][start_x + j] = tile
                    self.map_data[start_y + i][start_x + j] = tile


""" Example"""
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
