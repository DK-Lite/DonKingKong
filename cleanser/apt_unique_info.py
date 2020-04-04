
import json, re
import xmltodict
import pandas as pd
from os import path
from pymongo import MongoClient


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
        print("[Connect]: MongoDB")
    except Exception:
        print("[Connect]: Error")

    # Find
    db = client.data_warehouse
    colloction = db.apt_trade_info
    cursor = colloction.find()
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]

    print("all trade count : " + str(len(docs)))
    
    # cleanser
    output = dict()
    for doc in docs:
        key = doc['roadCityCode'] + doc['roadCode']
        output[key] = {
            "buildYear": doc["buildYear"],
            "lawName": doc["lawName"],
            "aptName": doc["aptName"],
            "lawTownCode": doc["lawTownCode"],
            "roadCityCode": doc["roadCityCode"],
            "roadCode": doc["roadCode"],
            "roadGroundCode": doc["roadGroundCode"],
            "roadMainCode": doc["roadMainCode"],
            "roadSubCode": doc["roadSubCode"],
        }
    
    print("apt count : " + str(len(output.keys())))

    # insert
    db = client.data_warehouse
    collection = db.apt_unique_info
    for _, doc in output.items():
        collection.insert(doc)
        
    client.close()

if __name__ == "__main__":
    main()
    
