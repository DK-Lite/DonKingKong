import os, json
from pymongo import MongoClient

DB_HOST     = "35.238.148.116"
DB_PORT     = 27017
ABS_PATH    = os.path.dirname(os.path.realpath(__file__))
PATH        = os.path.join(ABS_PATH, "data")

def change_key(dic, key, value):
    dic[key]=value
    return dic

def main():

    # MongoDB
    client = MongoClient(DB_HOST, DB_PORT)
    db = client.data_lake
    collection = db.apt_trade_info
    collection_date = db.apt_trade_date

    # get json_file_list in DIR (LOCAL)
    all_files = os.listdir(PATH)
    json_files = [ file for file in all_files if file.endswith(".json")]

    # get date_list in DB (MongoDB)
    cursor = collection_date.find()
    docs = [ change_key(doc,'_id', idx)['filename'] for idx, doc in enumerate(cursor)]

    # Loader 
    for file in json_files:
        # isExist?
        if file in docs: continue
        collection_date.insert({'filename': file })

        with open(os.path.join(PATH, file), "r") as json_file:
           apt_trade_infos = json.load(json_file)
        try:
            for apt_trade_info in apt_trade_infos:
                collection.insert(apt_trade_info)
        except Exception:
            print(apt_trade_info)

    # Close MongoDB
    client.close()
if __name__ == "__main__":
    main()
