from simulation import Simulation

if __name__ == '__main__':
    max_rounds = 50
    num_sheep = 15
    limit = 10.0
    sheep_movement = 0.5
    wolf_movement = 1.0

    simulation = Simulation(num_sheep, limit, wolf_movement, sheep_movement, max_rounds)
    simulation.run()
