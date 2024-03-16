import multiprocessing

def hi():
    return 1

def callback(result):
    print(f"Result: {result}")

def error_callback(error):
    print(f"Error: {error}")

if __name__ == '__main__':
    pool = multiprocessing.Pool()

    async_result = pool.apply_async(hi)
    pool.close()
    pool.join()

    print(async_result.get())
    """
    try:
        result = async_result.get()  # This is where errors will be raised if any occurred.
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
"""