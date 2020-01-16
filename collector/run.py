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
        for item in apt.DataReader(code, args.date):
            if item is None: continue
            requests.post("http://localhost:3691/data-lake/apt-trade-info", data=item.encode("utf-8"))
	

    #df_data = pd.concat([ apt.DataReader(code, args.date) for code in codes ], ignore_index=True)
    #df_data.to_csv("output.csv", encoding='utf-8-sig')
if __name__ == "__main__":
    main()
