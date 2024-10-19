import threading
import time  # Added to measure time

balance = 100
lock = threading.Lock()

def deposit(amount):
    global balance
    with lock:
        balance += amount
        print(f'Deposited: {amount}, New Balance: {balance}')

def withdraw(amount):
    global balance
    with lock:
        balance -= amount
        print(f'Withdrawn: {amount}, New Balance: {balance}')

# Start measuring time
start_time = time.time()

t1 = threading.Thread(target=deposit, args=(50,))
t2 = threading.Thread(target=withdraw, args=(30,))

t1.start()
t2.start()

t1.join()
t2.join()

# End measuring time
end_time = time.time()

# Calculate and print execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
