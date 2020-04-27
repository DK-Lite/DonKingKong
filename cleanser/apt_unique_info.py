
import json, re
import xmltodict
import pandas as pd
from os import path
from pymongo import MongoClient
from tqdm import tqdm

DB_HOST="localhost"
DB_PORT=27017

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

def change_key(dic, key, value):
    dic[key]=value
    return dic

def main():

    # MongoDB
    try:   
        client = MongoClient(DB_HOST, DB_PORT)
        print("Connect: MongoDB")
    except Exception:
        print("Connect: Error")

    # Find (Test)
    
    pipelines = list()
    pipelines.append({ 
        '$group': { 
            '_id': { 
                'day': { '$concat': ['$roadCityCode', '$roadCode'] },
            },
            "buildYear": {'$max' : '$buildYear'},
            "lawName": {'$max' : '$lawName'},
            "aptName": {'$max' : '$aptName'},
            "lawTownCode": {'$max' : '$lawTownCode'},
            "roadCityCode": {'$max' : '$roadCityCode'},
            "roadCode": {'$max' : '$roadCode'},
            "roadGroundCode": {'$max' : '$roadGroundCode'},
            "roadMainCode": {'$max' : '$roadMainCode'},
            "roadSubCode": {'$max' : '$roadSubCode'},    
        }
    })

    db = client.data_warehouse
    colloction = db.apt_trade_info
    cursor = db.apt_trade_info.aggregate(pipelines)
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]
    print("Group Count: "+len(docs))
    # insert
    db = client.data_warehouse
    collection = db.apt_unique_info
    for doc in tqdm(docs):
        cur = collection.find_one({
            'roadCityCode':doc['roadCityCode'],
            'roadCode':doc['roadCode'],
            })
        if not cur is None: continue
        
        collection.insert(doc)
       
        
    client.close()

if __name__ == "__main__":
    main()
    
