import requests
import json, argparse, xmltodict
from Loader import Loader
from AptDetail import *
from datetime import datetime, timedelta

#from bson.json_util import loads, dumps
# record = db.movies.find_one()
# json_str = dumps(record)
# record2 = loads(json_str)



def main():

    PATH = './data/'

    now = datetime.now() - timedelta(days=15)
    cur_date = now.strftime('%Y%m') 

    # argument 
    arg = argparse.ArgumentParser()
    arg.add_argument('--date', type=str, default=cur_date)
    args=arg.parse_args()
    
    print(args.date)
    # Loader 
    codes = Loader.get_codes()
    configs = Loader.get_configs()

    #data set
    apt = AptDetailReader(configs['service_key'])

    result = []
    for code in codes:
       items = apt.DataReader(code, args.date)
       if items is None: continue

       result.append(items)
       
       for item in items:
           requests.post("http://localhost:3691/data-lake/apt-trade-info", data=item)
	
    with open(PATH+cur_date+".json", "w", encoding="utf-8") as make_file:
        json.dump(result, make_file, ensure_ascii=False, indent="\t")


    #df_data = pd.concat([ apt.DataReader(code, args.date) for code in codes ], ignore_index=True)
    #df_data.to_csv("output.csv", encoding='utf-8-sig')
if __name__ == "__main__":
    main()
