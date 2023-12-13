import math


class Wolf:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def distance_to_sheep(self, sheep):
        return math.dist([sheep.x, sheep.y], [self.x, self.y])

    def move_wolf(self, sheep_list, wolf_step):
        nearest_sheep = sheep_list[0]
        nearest_sheep_dist = self.distance_to_sheep(nearest_sheep)

        for sheep in sheep_list:
            dist = self.distance_to_sheep(sheep)
            if dist < nearest_sheep_dist:
                nearest_sheep = sheep
                nearest_sheep_dist = dist

        if nearest_sheep_dist <= wolf_step:
            self.x = nearest_sheep.x
            self.y = nearest_sheep.y
            nearest_sheep.is_alive = False
        else:
            self.x += wolf_step * ((nearest_sheep.x - self.x) / nearest_sheep_dist)
            self.y += wolf_step * ((nearest_sheep.y - self.y) / nearest_sheep_dist)

        return nearest_sheep
