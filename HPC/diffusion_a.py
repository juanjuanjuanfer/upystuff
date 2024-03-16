from numpy import (zeros,roll)
import time

grid_shape = (600,600)

@profile
def evolve(grid, dt, D = 1.0):
    return grid + dt * D * laplacian(grid)

def laplacian(grid):
    return (roll(grid, 1, axis = 0) + 
            roll(grid, -1, axis = 0) + 
            roll(grid, 1, axis = 1) + 
            roll(grid, -1, axis = 1) - 
            4*grid)

@profile
def run_experiment(num_iterations):
    # Parameter Definition
    xmax, ymax = grid_shape
    grid = zeros(grid_shape)
    #Initial Conditions
    block_low = int(xmax * 0.4)
    block_high = int(xmax * 0.6)
    grid[block_low:block_high, block_low:block_high] = 0.005
    start = time.time()
    #Evolve Initial Conditions
    for i in range(num_iterations):
        grid = evolve(grid, 0.1, D = 1)
    return time.time() - start

run_experiment(500)