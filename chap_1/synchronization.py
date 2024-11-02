import threading
import time

def access_resource(thread_name):
    sem.acquire()
    print(f"{thread_name} accessing the resource")
    time.sleep(2)
    print(f"{thread_name} done")
    sem.release()

threads = []
sem = threading.Semaphore(1)

for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
