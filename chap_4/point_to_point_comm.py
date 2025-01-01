from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"My rank is: {rank}")

# Ensure the destination rank is within bounds
if rank == 0:
    data = 1000
    destination_process = 1  # Sending to process 1
    if destination_process < size:  # Check if the rank exists
        comm.send(data, dest=destination_process)
        print(f"Rank {rank} sent data {data} to process {destination_process}")
    else:
        print(f"Rank {rank}: Destination rank {destination_process} does not exist.")

if rank == 1:
    source_process = 0
    destination_process = 2  # Sending to process 2
    # Receive data from process 0
    if source_process < size:
        data = comm.recv(source=source_process)
        print(f"Rank {rank} received data: {data}")
    else:
        print(f"Rank {rank}: Source rank {source_process} does not exist.")
    # Send data to process 2
    if destination_process < size:
        comm.send("hello", dest=destination_process)
        print(f"Rank {rank} sent data 'hello' to process {destination_process}")
    else:
        print(f"Rank {rank}: Destination rank {destination_process} does not exist.")

if rank == 2:
    source_process = 1
    # Receive data from process 1
    if source_process < size:
        data = comm.recv(source=source_process)
        print(f"Rank {rank} received data: {data}")
    else:
        print(f"Rank {rank}: Source rank {source_process} does not exist.")

# Remove logic for ranks outside of the valid range
if rank == 8:  # This will never execute if rank 8 does not exist
    print(f"Rank {rank} should not execute because it is out of bounds.")
