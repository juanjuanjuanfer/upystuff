import multiprocessing

class Process(multiprocessing.Process):
    def __init__(self,counter, lock):
        super(Process, self).__init__()
        self.counter = counter
        self.lock = lock



    def run(self):
        for i in range(1_000):
            with self.lock:
                self.counter.value += 1

    
def main():
    counter = multiprocessing.Value('i', lock=True)
    lock = multiprocessing.Lock()
    process = [Process(counter,lock) for i in range(4)]

    [p.start() for p in process]
    [p.join() for p in process]
    
    print(counter.value)

if __name__ == '__main__':
    main()
