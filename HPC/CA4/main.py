

# pi_serial

#import random

def pi_serial(samples = 10000000):
    hits = 0
    for i in range(samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            hits += 1
    pi = 4.0 * hits / samples
    return pi

#print(pi_serial())

# pi_parallel

import multiprocessing
import random

def sample():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0


if __name__ == '__main__':

    samples = 1_000_000
    pool = multiprocessing.Pool()
    results_async = [pool.apply_async(sample) for i in range(samples)]
    pool.close()
    pool.join()    
    hits = sum(r.get() for r in results_async)
    pi = 4.0 * hits / samples
    print(pi)