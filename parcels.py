import requests
import json
import os
import time

PARCELS_URL = 'https://api.decentraland.org/v2/parcels/'
LINES = 150
TIMES = 15
PROC_N = 10


class Parcels():
    
    @staticmethod
    def retrieve_columns(x, y): #this method retrive and store in a directory all the parcels divided by column. The parallelism grade is now 10

        missed_parcels = []

        for i in range(x, x+TIMES+1): #loop on the columns
        
            ex = 0 
            json_array = []
            
            for j in range(y, LINES+1): #loop on the lines

                try:
                    p = requests.get(PARCELS_URL + str(i) + '/' + str(j))   
                    if ex != 0: # taking into account how many exceptions has been rised in a row
                        ex = 0
                    p_json = json.loads(str(p.text))
                    json_array.append(p_json)

                except:
                    ex =+ 1
                    print("Hello, I tried to retrive ("+str(i)+", "+str(j)+"), but I need to rest just "+str(ex*5)+' seconds...')
                    time.sleep(5*ex)

            with open("COLUMNS_JSON/column_"+ str(i) + ".json", "a+") as f: #open a file and store the parcels retrieved
                json.dump(json_array, f)
            print('Column '+str(i)+' fully retrieved')

        if missed_parcels != []: #open a file and store the cooridates of the missed parcels if there are any
            with open("COLUMNS_JSON/missed.json", 'a+') as m: 
                json.dump(missed_parcels, m)

    @staticmethod
    def parse_columns_ids(directory): #this method parse the columns retrived to get the ids. It stores all the parcels' id in different files divided by column
        
        counted_ids = 0
        ids = []

        for filename in os.scandir(directory): #loop on the files

            column = str(filename.split('_')[1].split('.')[0])

            if filename.is_file() and filename.endswith('.json'): # simple control on the file

                with open(filename, 'r') as f:
                    json_array = json.load(f)
                
                for parcel in json_array: #loop on the parcels into the opened file
                    counted_ids =+ 1 
                    ids.append(parcel['id'])
                
            with open('PARCELS_IDS/ids_'+column+'.json', 'a+') as i:
                i.dumps(ids)

            print(counted_ids)
                    