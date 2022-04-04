import multiprocessing
import time
import datetime

from parcels import Parcel
from orders import Order
from tiles import Tile
from estates import Estate
from wearable import Wearable
from multiprocessing import Process

PROC_N = 15
LINES = 300
TIMES = int(LINES/PROC_N)

string1 = "24/12/2019"
start = int(time.mktime(datetime.datetime.strptime(string1,"%d/%m/%Y").timetuple()))

if __name__ == '__main__':
    
    processes = []

    for i in range(-int(LINES/2),int(LINES/2), TIMES): #routine to retrive the parcels. This routine uses the official decentraland apis 
        print(i)
        p = Process(target=Parcel.retrieve_columns, args = (i,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

    #methods to retrive datas using TheGraph
    Wearable.retrieve_wearables() 
    Estate.retrieve_estate()
    Order.retrive_orders('parcel', 'open', start)
    Order.retrive_orders('parcel', 'sold', start)
    Order.retrive_orders('parcel', 'cancelled', start)
    Order.retrive_orders('estate', 'open', start)
    Order.retrive_orders('estate', 'sold', start)
    Order.retrive_orders('estate', 'cancelled', start)
    Order.retrive_orders('wearable', 'open', start)
    Order.retrive_orders('wearable', 'sold', start)
    Order.retrive_orders('wearable', 'cancelled', start)

    
