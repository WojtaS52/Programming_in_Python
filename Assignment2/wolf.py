import math


class Wolf:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def distance_to_the_nearest_sheep(self, sheep):
        dist = math.sqrt(((sheep.x - self.x)**2) + ((sheep.y - self.y)**2))
        return dist

    def move_wolf(self, sheeps_list, wolf_step):
        nearest_sheep = min(sheeps_list, key=lambda sheep: self.distance_to_the_nearest_sheep(sheep))

        if nearest_sheep:

            dist_to_sheep = self.distance_to_the_nearest_sheep(nearest_sheep)

            # Check if sheep is in available are for attack :C

            if wolf_step > dist_to_sheep:
                self.x = nearest_sheep.x
                self.y = nearest_sheep.y
                nearest_sheep.is_live = False       # :----(
            else:
                ratio = wolf_step / dist_to_sheep
                self.x += ratio * (nearest_sheep.x - self.x)
                self.y += ratio * (nearest_sheep.y - self.y)
