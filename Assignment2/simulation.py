from wolf import Wolf
from sheep import Sheep
import random
import json
import csv
import math


class Simulation:
    def __init__(self, number_of_sheep: int, limit: float, wolf_step: float, sheep_step: float, max_rounds: int):
        print('Start simulation')
        self.sheep_list = []
        for i in range(1, number_of_sheep + 1):
            self.sheep_list.append(Sheep(i, random.uniform(-limit, limit), random.uniform(-limit, limit)))

        self.sheep_step = sheep_step
        self.wolf_step = wolf_step
        self.wolf = Wolf()
        self.max_rounds = max_rounds

    def display_summary(self, round_num, chasing_sheep=None, eaten_sheep=None):
        print('\033[96m' + f'Round: {round_num}' + '\033[0m')
        print(f'Wolf Position: ({self.wolf.x:.3f}, {self.wolf.y:.3f})')

        if chasing_sheep:
            print(f'Wolf is chasing Sheep number(sid) {chasing_sheep.sid}')

        if eaten_sheep:
            print(f'Sheep number(sid) {eaten_sheep.sid} has been eaten by wolf')

        print(f'Number of Alive Sheep: {sum(sheep.is_live for sheep in self.sheep_list)} \n')

    def run(self):
        with open('alive.csv', 'w', newline='') as f_object:
            writer_object = csv.writer(f_object)
            writer_object.writerow(['round', 'alive_sheep'])
            f_object.close()

        json_data = []

        for round_num in range(1, self.max_rounds + 1):
            for sheep in self.sheep_list:
                if sheep.is_live:
                    sheep.sheep_move(self.sheep_step)

            alive_sheep = [sheep for sheep in self.sheep_list if sheep.is_live]

            self.wolf.move_wolf(alive_sheep, self.wolf_step)

            closest_sheep = min(alive_sheep, key=lambda s: self.wolf.distance_to_the_nearest_sheep(s))

            json_dict = {
                'round_no': round_num,
                'wolf_pos': (self.wolf.x, self.wolf.y),
                'sheep_pos': [(sheep.x, sheep.y) if sheep.is_live else None for sheep in self.sheep_list]
            }

            json_data.append(json_dict)

            if math.dist([self.wolf.x, self.wolf.y], [closest_sheep.x, closest_sheep.y]) <= self.wolf_step:
                self.display_summary(round_num, eaten_sheep=closest_sheep)
            else:
                self.display_summary(round_num, chasing_sheep=closest_sheep)

            number_of_alive_sheep = sum(sheep.is_live for sheep in self.sheep_list)

            with open('alive.csv', 'a', newline='') as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerow([round_num, number_of_alive_sheep])
                f_object.close()

            # Condition of end game
            if number_of_alive_sheep == 0:
                print('\033[92m' + 'Wolf has eaten every sheep in the meadow. The end of simulation' + '\033[0m')
                break

        with open('pos.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
