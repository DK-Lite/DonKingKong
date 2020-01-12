import json, argparse, xmltodict
import pandas as pd
from 


service_key = "&ServiceKey=aKVcsSF8UlpRkppSsPS38IZO8UZ87fNBzMTtrrWtoadmn7ySBos%2BX8AOc6M%2F47Temd2cIbpl4%2BFxq%2Btu0KoKWA%3D%3D"


for line in lines:
    LAWD_CD = line[0:-1]
    DEAL_YMD = "201912"
    w_filename = "./data/raw/{}.json".format(DEAL_YMD+"_"+LAWD_CD)
    numOfRows = "2000"
    
    print(LAWD_CD, DEAL_YMD)
    queryParams = '?' + urlencode({ \
        quote_plus('LAWD_CD') : LAWD_CD,
        quote_plus('DEAL_YMD') : DEAL_YMD,
        quote_plus('numOfRows') : numOfRows,
        })
    request = Request(url + queryParams + service_key)
    print(url + queryParams + service_key)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf8')

    with open(w_filename, "w", encoding="utf-8") as make_file:
       json.dump(xmltodict.parse(response_body), make_file, ensure_ascii=False, indent="\t")
    print("create file: " + w_filename)
    #with open(w_filename, "w", encoding="utf-8") as make_file:
    #    json.dump("[]", make_file, ensure_ascii=False, indent="\t")

    apt = AptDetailReader(service_key)
    df_data = apt.DataReader("41135", "201911")


   

def load_areacode(path):
    with open(path, 'r') as r_file:
        return r_file.readlines()

def main():

    arg = argparse.ArgumentParser()
    arg.add_argument('--date', type=str, default='-1')
    configs=arg.parse_args()

    codes = load_areacode("./area_code.txt")


    for code in codes:
        apt = AptDetailReader(service_key)
        df_data = apt.DataReader(code, configs.date)


if __name__ == "__main__":
    main()