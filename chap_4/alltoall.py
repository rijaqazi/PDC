from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

senddata = (rank+1)*np.arange(size,dtype=int)
recvdata = np.empty(size,dtype=int)

comm.Alltoall(senddata,recvdata)

print("process %s sending %s receiving %s" % (rank, senddata, recvdata))