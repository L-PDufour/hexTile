import os

from biome import *
from display import Display
from entity import Entity, Player
from map import Map


class Game:
    def __init__(self, player: Player, game_map: Map, display: Display) -> None:
        self._player = player
        self._game_map = game_map
        self._display = display

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, value: Player) -> None:
        self._player = value

    @property
    def game_map(self) -> Map:
        return self._game_map

    @game_map.setter
    def game_map(self, value: Map) -> None:
        self._game_map = value

    @property
    def display(self) -> Display:
        return self._display

    @display.setter
    def display(self, value: Display) -> None:
        self._display = value

    def start(self) -> None:
        self.intro()
        self.event()

    def event(self) -> None:
        self.game_map.map_data[self.game_map.player.y][
            self.game_map.player.x
        ].generate_event()
        current_biome = self.game_map.map_data[self.game_map.player.y][
            self.game_map.player.x
        ]
        if isinstance(current_biome, PlainsBiome):
            chance = 0.5
        else:
            chance = 0.3
        if random.random() < chance:
            enemy = Entity()
            self._player.set_fight_status(True)
            self._display.render_fight_screen(enemy)
            self._player.generate_loot()

    def intro(self) -> None:
        os.system("clear")
        frame_width = 50
        frame = "+" + "=" * (frame_width) + "+"

        print(frame)
        print(
            f"| {'Welcome to hexTile(forget about the hex) Game!':^{frame_width-2}} |"
        )
        print(f"| {'Your goal is to reach the town ⌂.':^{frame_width-2}} |")
        print(f"| {'You have options:':^{frame_width-2}} |")
        print(f"| {'1. Drink potions for health.':^{frame_width-2}} |")
        print(f"| {'2. Hunt for food.':^{frame_width-2}} |")
        print(f"| {'3. Manage your resources wisely.':^{frame_width-2}} |")
        print(f"| {'Running out of health or food leads to death.':^{frame_width-2}} |")
        print(f"| {'Running out of stamina means you cannot move.':^{frame_width-2}} |")
        print(f"| {'Every move costs stamina.':^{frame_width-2}} |")
        print(f"| {'Good luck on your adventure!':^{frame_width-2}} |")
        print(frame)

        player_name = input("Enter your hero name: ")
        print(f"Hello, {player_name}! Press enter to start.")
        input()

    # def fight(self, entity: Entity) -> None:
    #     while entity.health > 0 and self.player.health > 0:
    #         self.player.display_fight_status(entity)
    #         self.player.attack(entity)
    #         entity.attack(self.player)
    #     if self.player.health <= 0:
    #         print(f"{self.player.name} has died.")
    #         print("Game over.")
    #         exit()
    #     if entity.health <= 0:
    #         print(f"{entity.name} has died.")
    #         self.player.generate_loot()
