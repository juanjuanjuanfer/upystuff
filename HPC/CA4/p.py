import multiprocessing
import random

def sample():
    x, y = random.random(), random.random()
    return 1 if x*x + y*y <= 1 else 0

def sample_multiple(samples_partial):
    return sum(sample() for _ in range(samples_partial))

samples = 10000  # Total number of samples
n_tasks = 10
chunk_size = samples // n_tasks

# Using a context manager to ensure pools are properly closed
with multiprocessing.Pool() as pool:
    results_async = [pool.apply_async(sample_multiple, (chunk_size,)) for _ in range(n_tasks)]
    hits = sum(r.get() for r in results_async)

pi = 4.0 * hits / samples
print(pi)