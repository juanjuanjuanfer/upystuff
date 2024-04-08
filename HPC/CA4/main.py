import random
import multiprocessing

# pi_serial

def pi_serial(samples):
    hits = 0
    for i in range(samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            hits += 1
    pi = 4.0 * hits / samples
    return pi


# pi_apply_async

def sample():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0


<<<<<<< HEAD

if __name__ == '__main__':
=======
def pi_apply_async():
>>>>>>> 61fc53f2fec9b0118d355f5a3c05f368a24f346a
    samples = 1_000_000
    pool = multiprocessing.Pool()
    results_async = [pool.apply_async(sample) for i in range(samples)]
    pool.close()
    pool.join()    
    hits = sum(r.get() for r in results_async)
    return 4.0 * hits / samples



# pi_apply_async_chunked

def sample_multiple(samples_partial):
    return sum(sample() for _ in range(samples_partial))

def pi_apply_async_chunked(samples):
    n_tasks = 10
    chunk_size = samples // n_tasks
    pool = multiprocessing.Pool()

    results_async = [pool.apply_async(sample_multiple, (chunk_size,)) for _ in range(n_tasks)]
    hits = sum(r.get() for r in results_async)
    pool.close()
    pool.join()

    return 4.0 * hits / samples


