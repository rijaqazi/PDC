import concurrent.futures
import time

def count(number):
    for _ in range(0, 100000000):
        pass  # Empty loop for demonstration
    return number * 100000000

def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))

if __name__ == '__main__':
    number_list = list(range(1, 11))

    # Sequential Execution
    start_time = time.time()  # Use time.time() for better compatibility
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in %s seconds' % (time.time() - start_time))

    # Thread Pool Execution
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution in %s seconds' % (time.time() - start_time))

    # Process Pool Execution
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution in %s seconds' % (time.time() - start_time))