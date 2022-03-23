import requests
import json
import os
import time

TILES_URL = 'https://api.decentraland.org/v2/tiles'

class Tile():
    
    @staticmethod
    def retrieve_tiles(): #this method retrive and store in a directory all the parcels divided by column. The parallelism grade is now 10

        try:
            p = requests.get(TILES_URL)   
            with open('TILES_JSON/tiles.json', 'a+') as t:
                t.write(p.text)
            
        except Exception as e:
            print(e)
