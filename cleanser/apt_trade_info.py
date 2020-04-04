# get data in mongodb
# cleanser 
# set data
import re
from pymongo import MongoClient
from tqdm import tqdm

DB_HOST="localhost"
DB_PORT=27017
LOAD_DATA_SIZE=1000

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

def main():

    # MongoDB
    try:   
        client = MongoClient(DB_HOST, DB_PORT)
        print("Connect: MongoDB")
    except Exception:
        print("Connect: Error")

    # find
    db = client.data_lake
    collection = db.apt_trade_info

    data_warehouse = client.data_warehouse
    collection_warehouse = data_warehouse.apt_trade_info

    #{ $pop: { 필드1: ±1, 필드2: ±1, ... } }
    len = collection.find({'clean':{ '$exists': False}}).count()
    for i in tqdm(range(len)):
        doc = collection.find_and_modify(
            query= {'clean':{ '$exists': False }},
            #'sort'  : {name:1},
            #'remove': False,
            update= { "$set": { 'clean' : 1 }},
            new   = False,
            #'fields': {_id:0,name:1,age:1},
            upsert= False,
            #'bypassDocumentValidation': False
        )
        
#        collection_warehouse.insert_many({
#            'tradeValue' : cleanText(doc['거래금액']),
#            'buildYear' : doc['건축년도'],
#            'lawName' : doc['법정동'],
#            'dedicatedArea': doc['전용면적'],
#            'aptName' : cleanText(doc['아파트']),
#            'tradeYear': doc['년'],
#            'tradeMonth': doc['월'],
#            'tradeDay': doc['일'],
#            'roadCityCode': doc['도로명시군구코드'],
#            'lawTownCode': doc['법정동읍면동코드'],
#            'roadCode': doc['도로명코드'],
#            'roadGroundCode': doc['도로명지상지하코드'],
#            'roadMainCode': doc['도로명건물본번호코드'],
#            'roadSubCode': doc['도로명건물부번호코드'],
#        })

    client.close()

    
if __name__== "__main__":
    main()
