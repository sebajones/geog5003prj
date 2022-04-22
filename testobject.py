import random

class Object():
    def __init__ (self):
        self.y = None
        self.x = None
    def randomize(self):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)