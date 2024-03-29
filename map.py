import random
from random import randint

from biome import *
from entity import Player


class Map:
    def __init__(self, width: int, height: int, player: Player) -> None:
        self.width = width
        self.height = height
        self.map_data: list[list[Biome]] = []
        self.legend = []
        self.player = player

        self.generate_map()
        self.generate_patch(ForestBiome, 10, 2, 5)
        self.generate_patch(MountainsBiome, 5, 1, 5)
        self.generate_patch(WaterBiome, 2, 3, 5)
        self.generate_line(RiverBiome)
        self.map_data[0][randint(0, self.width - 1)] = TownBiome()

    def generate_map(self) -> None:
        self.map_data = [
            [PlainsBiome() for _ in range(self.width)] for _ in range(self.height)
        ]

    def generate_patch(
        self,
        biome_class,
        num_patches: int,
        min_size: int,
        max_size: int,
        irregular: bool = True,
    ) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(0, self.width - width)
            start_y = randint(0, self.height - height)

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = biome_class()

    def generate_line(self, biome) -> None:
        start_x, start_y = randint(0, self.width - 1), 0

        while start_y < self.height and start_x < self.width:
            self.map_data[start_y][start_x] = biome(self.map_data, start_x, start_y)
            if random.random() < 0.5:
                start_x += 1
            else:
                start_y += 1
