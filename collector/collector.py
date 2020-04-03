import requests, os
import json, argparse, xmltodict
import pandas
from Loader import Loader
from AptDetail import *
from datetime import datetime, timedelta
from tqdm.notebook import tqdm

def main():

    dt_index = pandas.date_range(start='20160101', end='20191201')
    dt_list = dt_index.strftime("%Y%m").tolist()
    dt_list = list(set(dt_list))
    dt_list.sort(reverse=True)

    abs_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(abs_path,"data")

    file_list = os.listdir(path)
    file_list_json = [ file for file in file_list if file.endswith(".json")]

    for dt in dt_list:
        if dt +'.json' not in file_list_json:
            cur_date = dt
            break

    print(f"Calling the data with {cur_date}") 

    PATH = os.path.join(abs_path,'data/'+str(cur_date)+'.json')

    # argument 
    arg = argparse.ArgumentParser()
    arg.add_argument('--date', type=str, default=cur_date)
    args=arg.parse_args()
    
    # Loader 
    codes = Loader.get_codes()
    configs = Loader.get_configs()

    #data set
    apt = AptDetailReader(configs['service_key'])

    result = []
    print("[Running...]")
    for code in tqdm(codes):
       items = apt.DataReader(code, args.date)
       if items is None: continue
       result += items
       
    with open(PATH, "w", encoding="utf-8") as make_file:
        json.dump(result, make_file, ensure_ascii=False, indent="\t")

if __name__ == "__main__":
    main()
