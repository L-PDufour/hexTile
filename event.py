class Event:
    def __init__(self, name, date, location, description):
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.date} - {self.location} - {self.description}"
