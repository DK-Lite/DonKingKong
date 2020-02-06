# get data in mongodb
# cleanser 
# set data
import re
from pymongo import MongoClient
from tqdm import tqdm_notebook


def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

def main():
    client = MongoClient("34.84.195.184", 17017)

    # find
    db = client.data_lake
    colloction = db.apt_trade_info
    cursor = colloction.find({'is_clean': { '$exists': False }})
    docs = [ doc for idx, doc in enumerate(cursor)]

    # update
    colloction.update({'is_clean': { '$exists': False }}, { "$set": { 'is_clean' : 1 }}, multi=True)    

    # cleansing
    clean_docs = []
    for doc in docs:
        try:
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
        except:
            print(doc)

    # insert
    db = client.data_warehouse
    collection = db.apt_trade_info
    for doc in clean_docs:
        collection.insert(doc)
    client.close()

    
if __name__== "__main__":
    main()



# doc['trade_value'] = doc.pop('거래금액')
# doc['build_year'] = doc.pop('건축년도')
# doc['trade_year'] = doc.pop('년')
# doc['road_name'] = doc.pop('도로명')
# doc['road_main_code'] = doc.pop('도로명건물본번호코드')
# doc['road_sub_code'] = doc.pop('도로명건물부번호코드')
# doc['road_serial_num_code'] = doc.pop('도로명일련번호코드')
# doc['road_ground_code'] = doc.pop('도로명지상지하코드')
# doc['road_city_code'] = doc.pop('도로명시군구코드')
# doc['road_code'] = doc.pop('도로명코드')
# doc['law_name'] = doc.pop('법정동')
# doc['law_main_code'] = doc.pop('법정동본번코드')
# doc['law_sub_code'] = doc.pop('법정동부번코드')
# doc['law_city_code'] = doc.pop('법정동시군구코드')
# doc['law_town_code'] = doc.pop('법정동읍면동코드')
# doc['law_area_num_code'] = doc.pop('법정동지번코드')
# doc['apt_name'] = cleanText(doc.pop('아파트'))
# doc['trade_month'] = doc.pop('월')
# doc['trade_day'] = doc.pop('일')
# doc['serial_num'] = doc.pop('일련번호')
# doc['dedicated_area'] = doc.pop('전용면적')
# doc['area_num'] = doc.pop('지번')
# doc['area_cdoe'] = doc.pop('지역코드')
# doc['apt_layer'] = doc.pop('층')