import requests
import json
import pandas as pd
import time
import sqlite3

from datetime import date
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


# Select your transport with a defined url endpoint
transport = RequestsHTTPTransport(url="https://api.thegraph.com/subgraphs/name/decentraland/marketplace")
# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)


class Wearable():
    
    @staticmethod
    def retrieve_wearables(): # method to retrive orders given the starting udating timestamp and the final updating timestamp
        
        with open('WEARABLES/wearables.json', 'a+') as w: # restriveing the first wearable
            
            mystring = """
            {
                wearables (where:{id_gt:"wearable-0x09305998a531fade369ebe30adf868c96a34e813-0"}){
                    id
                    owner {
                        id
                    }
                    name
                    category
                    rarity
                    nft {
                        id
                    }
                }
            }
            """

            try:
                query = gql(mystring)
                result = client.execute(query)
                w.write(json.dumps(result)+'\n')

            except e:
                print('oh no1!')
                print(e)
                return

            id = 'wearable-0x09305998a531fade369ebe30adf868c96a34e813-0'
                
            while True:
                #composing the gql query string inserting the last update i stored
                mystring = """
                {
                    wearables (first:1000 orderBy:id orderDirection:asc where:{id_gt:\""""+id+"""\"}){
                        id
                        owner {
                            id
                        }
                        name
                        category
                        rarity
                        nft {
                            id
                        }
                    }
                }
                """

                try:

                    query = gql(mystring)
                    result = client.execute(query)

                    if result['wearables'] == []: #if there are no retrieved datas   
                        break
                    id = str(result['wearables'][-1]['id'])
                    w.write(json.dumps(result)+'\n')

                except e:
                    print('oh no2!')
                    print(e)
                    break
        print('done!')
