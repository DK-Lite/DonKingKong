
import json, re
import xmltodict
import pandas as pd
from pymongo import MongoClient

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

def change_key(dic, key, value):
    dic[key]=value
    return dic

def main():
    client = MongoClient("34.84.195.184", 17017)

    # find
    db = client.data_warehouse
    colloction = db.apt_trade_info
    cursor = colloction.find()
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]

    client.close()

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
    
    with open("apt_unique_info.json", "w", encoding="utf-8") as make_file:
        json.dump(output, make_file, ensure_ascii=False, indent="\t")

if __name__ == "__main__":
    main()
    