import math


class Wolf:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def distance_to_the_nearest_sheep(self, sheep):
        return math.dist([sheep.x, sheep.y], [self.x, self.y])

    def move_wolf(self, sheep_list, wolf_step):
        nearest_sheep = min(sheep_list, key=lambda sheep: self.distance_to_the_nearest_sheep(sheep))

        if nearest_sheep:

            dist_to_sheep = self.distance_to_the_nearest_sheep(nearest_sheep)

            if dist_to_sheep <= wolf_step:
                self.x = nearest_sheep.x
                self.y = nearest_sheep.y
                nearest_sheep.is_live = False
            else:
                self.x += wolf_step / dist_to_sheep * (nearest_sheep.x - self.x)
                self.y += wolf_step / dist_to_sheep * (nearest_sheep.y - self.y)
