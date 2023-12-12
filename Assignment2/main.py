from simulation import Simulation

if __name__ == '__main__':
    num_sheep = 10
    limit = 10.0
    wolf_movement = 1.0
    sheep_movement = 0.5
    max_rounds = 50

    simulation = Simulation(num_sheep, limit, wolf_movement, sheep_movement, max_rounds)
    simulation.run()

