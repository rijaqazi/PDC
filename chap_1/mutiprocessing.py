from do_something import *
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 10000000
    procs = 12
    jobs = []

    # Multiprocessing
    start_time = time.time()
    for i in range(procs):
        out_list = list()
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)

    # Reset jobs list for threading
    jobs = []
    
    # Multithreading
    start_time = time.time()
    threads = 12
    for i in range(threads):
        out_list = list()
        thread = threading.Thread(target=do_something, args=(size, out_list))  
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)
