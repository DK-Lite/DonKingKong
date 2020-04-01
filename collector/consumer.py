import os, json
from pymongo import MongoClient

DB_HOST = "34.84.195.184"
DB_PORT = 27017
def main():

    # MongoDB
    client = MongoClient(DB_HOST, DB_PORT)
    db = client.data_lake
    collection = db.apt_trade_info

    # PATH
    abs_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(abs_path, "data")

    # get json_file_list
    all_files = os.listdir(path)
    json_files = [ file for file in all_files if file.endswith(".json")]
    
    # Loader 
    for file in json_files:
        with open(os.path.join(path, file), "r") as json_file:
           apt_trade_infos = json.load(json_file)
        
        for apt_trade_info in apt_trade_infos:
            collection.insert(apt_trade_info)

    # Close MongoDB
    client.close()
if __name__ == "__main__":
    main()
