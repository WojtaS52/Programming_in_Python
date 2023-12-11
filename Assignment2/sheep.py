import random


class Sheep:
    def __init__(self, sid, x, y):
        self.sid = sid
        self.x = x
        self.y = y
        self.is_live = True

    def sheep_move(self, dist):
        # TODO: change on like in instruction up ~ north, ect?

        direct = random.choice(['up', 'down', 'left', 'right'])

        if direct == 'up':
            self.y = self.y + dist
        elif direct == 'down':
            self.y = self.y - dist
        elif direct == 'left':
            self.x = self.x - dist
        elif direct == 'right':
            self.x = self.x + dist