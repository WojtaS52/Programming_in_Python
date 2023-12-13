import random


class Sheep:
    def __init__(self, sid, x, y):
        self.sid = sid
        self.x = x
        self.y = y
        self.is_alive = True

    def sheep_move(self, dist):
        direct = random.choice(['north', 'south', 'west', 'east'])

        if direct == 'north':
            self.y = self.y + dist
        elif direct == 'south':
            self.y = self.y - dist
        elif direct == 'west':
            self.x = self.x - dist
        elif direct == 'east':
            self.x = self.x + dist
