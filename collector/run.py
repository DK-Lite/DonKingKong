import json, argparse, xmltodict
import pandas as pd
from Loader import Loader
from AptDetail import *

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
    df_data = pd.concat([ apt.DataReader(code, args.date) for code in codes ], ignore_index=True)
    df_data.to_csv("output.csv", encoding='utf-8-sig')

if __name__ == "__main__":
    main()