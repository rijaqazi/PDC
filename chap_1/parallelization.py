import numpy as np
from concurrent.futures import ThreadPoolExecutor
import time

# Function to add a slice of the vectors
def vector_add_slice(start, end, a, b, c):
    c[start:end] = a[start:end] + b[start:end]

# Host code
N = 10**6
a = np.random.random(N).astype(np.float32)
b = np.random.random(N).astype(np.float32)
c = np.empty(N, dtype=np.float32)

# Define the number of threads
threads = 8  # Adjust based on your system's cores
chunk_size = N // threads

# Timing
start_time = time.time()

# Using ThreadPoolExecutor for parallelism
with ThreadPoolExecutor(max_workers=threads) as executor:
    futures = []
    for i in range(threads):
        start = i * chunk_size
        end = N if i == threads - 1 else (i + 1) * chunk_size
        futures.append(executor.submit(vector_add_slice, start, end, a, b, c))
    
    # Wait for all threads to finish
    for future in futures:
        future.result()

end_time = time.time()
print(f"Time taken for parallel computation: {end_time - start_time:.3f} seconds")

# Verify result and print the first 10 elements
np.testing.assert_array_equal(c, a + b)
print(f"First 10 elements of result: {c[:10]}")
