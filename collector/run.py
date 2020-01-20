import requests
import json, argparse, xmltodict
from Loader import Loader
from AptDetail import *

#from bson.json_util import loads, dumps
# record = db.movies.find_one()
# json_str = dumps(record)
# record2 = loads(json_str)

def main():
    # argument 
    arg = argparse.ArgumentParser()
    arg.add_argument('--date', type=str, default='-1')
    args=arg.parse_args()

    # Loader 
    codes = Loader.get_codes()
    configs = Loader.get_configs()

    # data set
    apt = AptDetailReader(configs['service_key'])
    for code in codes:
        items = apt.DataReader(code, args.date)
        if items is None: continue
        for item in items:
            requests.post("http://localhost:3691/data-lake/apt-trade-info", data=item)
	

    #df_data = pd.concat([ apt.DataReader(code, args.date) for code in codes ], ignore_index=True)
    #df_data.to_csv("output.csv", encoding='utf-8-sig')
if __name__ == "__main__":
    main()
