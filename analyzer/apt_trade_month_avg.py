
import json, time
import xmltodict
import pandas as pd
from pymongo import MongoClient
from tqdm import tqdm

DB_HOST="localhost"
DB_PORT=27017


def change_key(dic, key, value):
    dic[key]=value
    return dic

class AptLocationAPI:
    def __init__(self):
        pass


def main():

    try:
        client = MongoClient(DB_HOST, DB_PORT)
        db = client.data_warehouse
        print("Connect: MongoDB")
    except Exception:
        print("Connect: Error")

    # find
    pipelines = list()
    pipelines.append({ 
        '$group': { 
            '_id': { 
                'day': { '$concat': ['$tradeYear', '-', '$tradeMonth'] }, 
            #   'name': "$aptName", 
                'area': '$dedicatedArea', 
            #    'roadCityCode': '$roadCityCode',
            #    'roadCode': '$roadCode',
            },
            'aptName': { '$max' : '$aptName' },
            'value': { '$avg': { '$toInt' : '$tradeValue'} },
            'roadCityCode': { '$max' : '$roadCityCode'} ,
            'roadCode': {'$max' : '$roadCode'} ,
        }
    })

    cursor = db.apt_trade_info.aggregate(pipelines)
    docs = [ doc for idx, doc in enumerate(cursor)]
    
    db = client.data_mart
    db.apt_trade_month_avg.drop()
    db.apt_trade_month_avg.insert_many(docs)

    client.close()

if __name__ == "__main__":
    main()
    
