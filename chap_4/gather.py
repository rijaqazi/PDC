from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = None  # Placeholder for data received from other processes
else:
    data = (rank + 1) ** 2  # Calculate data to send (square of rank + 1)

data = comm.gather(data, root=0)

if rank == 0:
    for i in range(1, size):
        print(f"process 0 receiving {data[i]} from process {i}")