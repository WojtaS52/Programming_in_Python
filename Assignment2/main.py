


from simulation import Simulation

if __name__ == '__main__':

    #szybki main do testu
    num_sheep = 15
    limit = 10.0
    sheep_movement = 0.5
    wolf_movement = 1.0
    max_rounds = 50

    simulation = Simulation(num_sheep, limit, sheep_movement, wolf_movement, max_rounds)
    simulation.run()