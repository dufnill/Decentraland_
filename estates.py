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


class Estate():
    
    @staticmethod
    def retrieve_estate(): # method to retrive orders given the starting udating timestamp and the final updating timestamp
        
        tkId = 1

        with open('ESTATES/estates.json', 'a+') as w:
                
            while True:
                #composing the gql query string inserting the last update i stored
                mystring = """
                {
                    estates (first:1000 orderBy:tokenId orderDirection:asc where:{tokenId_gt:"""+str(tkId)+"""}) {
                        id
                        tokenId
                        owner {
                            id
                        }
                        data {
                            id
                        }
                        rawData
                        nft {
                            id
                        }
                    }
                }
                """

                try:

                    query = gql(mystring)
                    result = client.execute(query)

                    if result['estates'] == []: #if there are no retrieved datas   
                        break
                    tkId = tkId + 1000
                    w.write(json.dumps(result)+'\n')

                except:

                    print('oh no!')

