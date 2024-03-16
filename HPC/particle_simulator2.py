import matplotlib.pyplot as plt
from matplotlib import animation
from random import uniform
import numpy as np

class Particle:
    def __init__(self, x, y, angular_velocity):
        self.x = x
        self.y = y
        self.angular_velocity = angular_velocity

class Particle_Simulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)
        for i in range(nsteps):
            for p in self.particles:
                d_x = timestep * p.y * p.angular_velocity / (p.x**2 + p.y**2)**0.5
                d_y = - timestep * p.x * p.angular_velocity / (p.x**2 + p.y**2)**0.5

                p.x += d_x
                p.y += d_y


def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        # We let the particle evolve for 0.01 time units.
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=10, blit=True)
    
    plt.show()

def test_visualize():
    particles = [Particle(0.3, 0.5, 1.0), 
                 Particle(0.0, -0.5, -1), 
                 Particle(-0.1, -0.4, 3)]
    
    simulator = Particle_Simulator(particles)

    visualize(simulator)

def benchmark():
    particles = [(Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-10.0, 10.0))) for i in range(100)]
    
    simulator = Particle_Simulator(particles)

    simulator.evolve(0.1)

if __name__ == '_main_':
    benchmark()
    '''
    import timeit
    """
    result = timeit.timeit("benchmark()", 
                    setup="from _main_ import benchmark", 
                    number=5,
                    repeat=4)
    print(result)
    """
    result = timeit.repeat("benchmark()",
                           setup="from _main_ import benchmark",
                           number=5,
                           repeat=4)
    #print(result)
    result = np.array(result)/5
    mean = np.mean(result)
    std = np.std(result)
    print("T={} \u00B1 {}s".format(mean, std))

#checar el tiempo
#python -m timeit -s "import particle_simulator" "particle_simulator.benchmark()"'''