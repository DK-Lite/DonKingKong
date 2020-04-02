
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
    client = MongoClient(DB_HOST, DB_PORT)

    # find
    db = client.data_warehouse
    colloction = db.apt_trade_info
    cursor = colloction.find()
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]

    print("all trade count : " + str(len(docs)))
    
    # cleanser
    output = dict()
    for doc in docs:
        key = doc['road_city_code'] + doc['road_code']
        output[key] = {
            "build_year": doc["build_year"],
            "law_name": doc["law_name"],
            "apt_name": doc["apt_name"],
            "law_town_code": doc["law_town_code"],
            "road_city_code": doc["road_city_code"],
            "road_code": doc["road_code"],
            "road_ground_code": doc["road_ground_code"],
            "road_main_code": doc["road_main_code"],
            "road_sub_code": doc["road_sub_code"],
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
    
