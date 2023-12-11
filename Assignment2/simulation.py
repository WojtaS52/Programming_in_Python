import math

from wolf import Wolf
from Assignment2.sheep import Sheep
import random


class Simulation:
    def __init__(self, number_of_sheep: int, limit: float, wolf_step: float, sheep_step: float, max_rounds: int):
        self.sheep_list = [Sheep(i, random.uniform(-limit, limit), random.uniform(-limit, limit)) for i
                           in range(1, number_of_sheep + 1)]
        self.sheep_step = sheep_step
        self.wolf_step = wolf_step
        self.wolf = Wolf()
        self.max_rounds = max_rounds

    def display_summary(self, round_num, chasing_sheep=None, eaten_sheep=None):

        print(f"Round: {round_num}")
        print(f"Wolf Position: ({self.wolf.x:.3f}, {self.wolf.y:.3f})")
        print(f"Number of Alive Sheep: {sum(sheep.is_live for sheep in self.sheep_list)}")

        if chasing_sheep:
            print(f"Wolf is chasing Sheep {chasing_sheep.sid}")

        if eaten_sheep:
            print(f"Sheep {eaten_sheep.sid} has been eaten")

    def run(self):
        for round_num in range(1, self.max_rounds + 1):
            for sheep in self.sheep_list:
                if sheep.is_live:
                    sheep.sheep_move(self.sheep_step)

            self.wolf.move_wolf([sheep for sheep in self.sheep_list if sheep.is_live], self.wolf_step)

            closest_sheep = min([sheep for sheep in self.sheep_list if sheep.is_live], key=lambda sheep: self.wolf.distance_to_the_nearest_sheep(sheep))

            if math.sqrt(
                    (self.wolf.x - closest_sheep.x) ** 2 + (self.wolf.y - closest_sheep.y) ** 2) <= self.wolf_step:
                closest_sheep.is_live = False
                self.display_summary(round_num, eaten_sheep=closest_sheep)
            else:
                self.display_summary(round_num, chasing_sheep=closest_sheep)

            #Condiotion of end game (idk why i think about avengers)
            if sum(sheep.is_live for sheep in self.sheep_list) == 0:
                print("All sheep have been eaten. Simulation ends.")
                break
