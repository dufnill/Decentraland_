import multiprocessing

from parcels import Parcel
from tiles import Tile
from multiprocessing import Process


PROC_N = 15
LINES = 300
TIMES = int(LINES/PROC_N)

if __name__ == '__main__':
    
    processes = []

    for i in range(-int(LINES/2),int(LINES/2), TIMES):
        print(i)
        p = Process(target=Parcel.retrieve_columns, args = (i,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()



    