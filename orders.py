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

class Order():

    @staticmethod
    def retrive_orders(category, status, start): # method to retrive orders given the starting udate timestamp, category to retrieve and the order's status
        if category not in ['parcel', 'estate', 'wearable']:
            return 'Choose a category between <parcel, estate, wearable>'
        if status not in ['open', 'sold', 'cancelled']:
            return 'Choose a status between <open, sold, cancelled>'

        with open(category.upper()+'/'+category+'_'+status+'.json', 'a+') as w:
    
            while True:
                
                #composing the gql query string inserting the last update i stored
                mystring = """
                {
                    orders (first: 1000 orderBy: updatedAt orderDirection: asc where: {category:"""+category+""" status:"""+status+""" updatedAt_gt:"""+str(start)+"""}) {
                        id
                        category
                        nft {
                            id
                        }
                        nftAddress
                        tokenId
                        txHash
                        owner
                        buyer
                        price
                        blockNumber
                        expiresAt
                        createdAt
                        updatedAt
                    }
                }
                """

                try:

                    query = gql(mystring)
                    result = client.execute(query)
                
                    if result['orders'] == []: #if there are no retrieved datas   
                        break
                    start = int(result['orders'][-1]['updatedAt']) + 1
                    w.write(json.dumps(result)+'\n')

                except:

                    print('oh no!')