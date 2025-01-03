## Chapter 1: Parallel Programming in Python

This chapter introduces key concepts of parallel programming using Python. It focuses on process creation, inter-process communication, synchronization, and shared memory to build efficient and scalable applications. Below is a breakdown of the files included in this chapter with their descriptions.

## File Descriptions

1. bank.py

Implements a basic banking system simulation with shared resources, demonstrating race conditions and strategies to handle them.

2. data_parallelism.py

Introduces data parallelism, showcasing how to distribute data across multiple processes for concurrent computations.

3. do_something.py

A simple script illustrating the concept of parallel tasks using Python's multiprocessing module.

4. fibonacci.py

Demonstrates parallel computation by distributing the calculation of Fibonacci numbers across multiple processes.

5. hello.py

A classic "Hello, World!" example for parallel programming, where multiple processes print messages concurrently.

6. ipc.py

Covers Inter-Process Communication (IPC) techniques such as pipes and queues for data exchange between processes.

7. mpi.py

Introduces the basics of Message Passing Interface (MPI) using Python’s mpi4py library for distributed computing.

8. multiprocessing.py

Explores the multiprocessing module in Python for creating and managing multiple processes.

9. parallelization.py

Focuses on techniques for parallelizing computational tasks to improve performance.

10. process_creation.py

Provides examples of process creation and management using Python’s os and multiprocessing modules.

11. shared_mem.py

Explains the use of shared memory for efficient data sharing between processes, avoiding unnecessary copying.

12. synchronization.py

Covers synchronization mechanisms like locks, semaphores, and barriers to ensure safe access to shared resources.

How to Use

Clone or download the repository containing these scripts.

Ensure you have Python installed, preferably version 3.8 or higher.

Install required dependencies (e.g., mpi4py for MPI-related examples).

Run the scripts individually to understand each concept.

Additional Notes

Each file is self-contained and includes comments to help understand the underlying concepts.

Experiment with modifying the scripts to see how changes affect performance and behavior.

Happy coding!