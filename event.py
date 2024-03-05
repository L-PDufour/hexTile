from tile import Tile


class Event:
    def __init__(self):
        self = self
        # self.date = date
        # self.location = location
        # self.description = description

    def display_event(self, event_message: str) -> None:
        frame_width = len(event_message) + 2
        frame = "+" + "=" * frame_width + "+"
        padding = "|" + " " * (frame_width) + "|"

        print(frame)
        print(padding)
        print(f"| {event_message} |")
        print(padding)
        print(frame)

    def handler(self, tile: Tile) -> None:
        if tile.symbol == ".":
            print("You are in a plain.")
            self.display_event("You are in a plain.")
        # elif tile.symbol == forest:
        # self.display_event("You are in a forest.")
        # self.plains_event()
        # event = self.get_event()
        # self.display_event(event)

    def get_event(self) -> str:
        pass
