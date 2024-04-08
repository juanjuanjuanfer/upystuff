import matplotlib.pyplot as plt
from matplotlib import animation
from random import uniform
import numpy as np
import matplotlib.cm as cm

class Particle:
    def __init__(self, x, y, angular_speed):
        self.x = x
        self.y = y
        self.angular_speed = angular_speed

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles
    
    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)
        
        for i in range(nsteps):
            for p in self.particles:
                norm = (p.x**2 + p.y**2)**0.5
                d_x = timestep * p.angular_speed * p.y / norm
                d_y = -timestep * p.angular_speed * p.x / norm
                
                p.x += d_x
                p.y += d_y

def visualize(simulator):
    angular_speeds = [abs(p.angular_speed) for p in simulator.particles]
    max_angular_speed = max(angular_speeds)

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    colormap = cm.Greens

    sizes = [(speed / max_angular_speed) * 100 for speed in angular_speeds]  # Adjust size factor as needed

    scatter = ax.scatter([p.x for p in simulator.particles],
                         [p.y for p in simulator.particles],
                         c=[colormap(speed / max_angular_speed) for speed in angular_speeds],
                         s=sizes)  # size parameter

    def animate(i):
        simulator.evolve(0.01)
        x = [p.x for p in simulator.particles]
        y = [p.y for p in simulator.particles]
        angular_speeds = [abs(p.angular_speed) for p in simulator.particles]
        sizes = [(speed / max_angular_speed) * 100 for speed in angular_speeds]

        scatter.set_offsets(np.c_[x, y])
        scatter.set_color([colormap(speed / max_angular_speed) for speed in angular_speeds])
        scatter.set_sizes(sizes)

        return scatter,

    anim = animation.FuncAnimation(fig, animate, blit=True, interval=10)
    plt.show()

def test_visualize():
    particles = [Particle(0.3, 0.5, 1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, 3)]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

def benchmark():
    particles = [Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-10.0, 10.0)) for i in range(50)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
    visualize(simulator)

if __name__ == '__main__':
    benchmark()
