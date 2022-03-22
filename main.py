import multiprocessing

from parcels import Parcels
from multiprocessing import Process, Pool


TIMES = 15
PROC_N = 10

if __name__ == '__main__':
    
    processes = []

    for i in range(0, PROC_N):
        p = Process(target=Parcels.retrieve_columns, args = (i*TIMES, 0,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

    