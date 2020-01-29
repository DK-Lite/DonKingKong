# get data in mongodb
# cleanser 
# set data
import json
from pymongo import MongoClient


def main():
    client = MongoClient("34.84.195.184", 17017)
    db = client.data_lake
    colloction = db.apt_trade_info
    cursor = colloction.find()
    docs = [ doc for idx, doc in enumerate(cursor)]
    print(docs)
    
    with open("output.json", "w", encoding="utf-8") as make_file:
        json.dump(docs, make_file, ensure_ascii=False, indent="\t")

    
if __name__== "__main__":
    main()
