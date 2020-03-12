
import re
from pymongo import MongoClient
from tqdm import tqdm_notebook

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

def change_key(dic, key, value):
    dic[key]=value
    return dic


            clean_docs.append({
                'trade_value' : cleanText(doc['거래금액']),
                'build_year' : doc['건축년도'],
                'law_name' : doc['법정동'],
                'dedicated_area': doc['전용면적'],
                'apt_name' : cleanText(doc['아파트']),
                'trade_year': doc['년'],
                'trade_month': doc['월'],
                'trade_day': doc['일'],
                'road_city_code': doc['도로명시군구코드'],
                'law_town_code': doc['법정동읍면동코드'],
                'road_code': doc['도로명코드'],
                'road_ground_code': doc['도로명지상지하코드'],
                'road_main_code': doc['도로명건물본번호코드'],
                'road_sub_code': doc['도로명건물부번호코드'],
            })


        output[key] = {
            "build_year": doc["build_year"],
            "law_name": doc["law_name"],
            "apt_name": doc["apt_name"],
            "law_town_code": doc["law_town_code"],
            "road_city_code": doc["road_city_code"],
            "road_code": doc["road_code"],
            "road_ground_code": doc["road_ground_code"],
            "road_main_code": doc["road_main_code"],
            "road_sub_code": doc["road_sub_code"],
        }



{
    "apt_name":,


}


{
    'apt_name' : "",
    'yyyydds' {}
    'dataset': [
        {
        'label': 'dedicated_area',
        'data': {'meanprices'},
        },
    ]
}

# date, area group by




def main():
    client = MongoClient("34.84.195.184", 17017)

    # find
    db = client.data_warehouse

    colloction = db.apt_unique_info
    cursor = colloction.find()
    docs = [ doc for idx, doc in enumerate(cursor)]

    colloction = db.apt_trade_info
    cursor = colloction.find()
    apt_docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]
    
    for doc in docs:
        apt_name = doc["apt_name"]
        cursor = colloction.find({'apt_name': apt_name })
        apt_docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]

        


    # analyzer 


    # data insert
    # insert
    db = client.data_mart
    collection = db.trade_mean_price
    for doc in clean_docs:
        collection.insert(doc)
    client.close()


    

if __name__ == "__main__":
    main()
    
