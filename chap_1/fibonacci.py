import threading
import time

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)

threads = []
start_time = time.time()
for i in range(9):  # 4 threads
    t = threading.Thread(target=calc_fibonacci, args=(35,))
    threads.append(t)

    print(f"Starting thread {i + 1}")
    t.start()

for t in threads:
    t.join()
    
end_time = time.time()
print(f"threads execution time:{end_time - start_time} seconds")
