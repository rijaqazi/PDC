from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
else:
    array_to_share = None
    recvbuf = None  # Initialize recvbuf for non-root processes

recvbuf = comm.scatter(array_to_share, root=0) 

if recvbuf is not None:
    print("process = %d" % rank + " recvbuf = %d " % recvbuf)
else:
    print("process = %d" % rank + " No data received.")