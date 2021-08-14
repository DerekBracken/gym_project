class Session:

    def __init__(self, name, description, time, day, capacity, id=None):
        self.name = name
        self.description = description
        self.time = time
        self.day = day
        self.capacity = capacity
        self.id = id
