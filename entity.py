class Entity:
    def __init__(self, name, health, x, y):
        self.name = name
        self.maxhealth = health
        self.health = health
        self.symbol = "@"
        self.x = x
        self.y = y
