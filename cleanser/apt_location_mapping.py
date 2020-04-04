
import json, time
import xmltodict
import pandas as pd
from os import path
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request
from common.geo import *
from pymongo import MongoClient
from tqdm import tqdm

DB_HOST="localhost"
DB_PORT=27017
class AptLocationAPI:
    URL = 'http://www.juso.go.kr/addrlink/addrCoordApi.do'
    def __init__(self, service_key):
        self.service_key = service_key

    def DataReader(self, 
        admCd=None, 
        rnMgtSn=None, 
        udrtYn=None, 
        buldMnnm=None, 
        buldSlno=None):

        queryParams = '?' + urlencode({ \
            quote_plus('confmKey') : self.service_key,  # 승인키
            quote_plus('admCd') : admCd, # 행정구역코드
            quote_plus('rnMgtSn') : rnMgtSn, # 도로명코드
            quote_plus('udrtYn') : udrtYn, # 지하여부
            quote_plus('buldMnnm') : buldMnnm, # 건물본번
            quote_plus('buldSlno') : buldSlno, # 건물부번
            quote_plus('resultType'): json,
            })

        request = Request(self.URL + queryParams + self.service_key)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode('utf8')
        json_data = xmltodict.parse(response_body)

        self.data = json_data

    def getXY(self):
        try:
            X = self.data["results"]["juso"]["entX"]
            Y = self.data["results"]["juso"]["entY"]
            return utmk_to_grs80(X, Y)
        except:
            return 0, 0

def main():

    apt = AptLocationAPI("devU01TX0FVVEgyMDIwMDIwNjIzMDE1MjEwOTQ0NzQ=")
    try:
        client = MongoClient(DB_HOST, DB_PORT)
        print("Connect: MongoDB")
    except Exception:
        print("Connect: Error")

    # find
    db = client.data_warehouse
    colloction = db.apt_unique_info
    cursor = colloction.find({'longitude': { '$exists': False }})
    docs = [ doc for idx, doc in enumerate(cursor)]

    # cleansing
    for doc in tqdm(docs):
        time.sleep(1)
        inputs = {
            'admCd' : doc['roadCityCode'] + doc['lawTownCode'],
            'rnMgtSn' : doc['roadCityCode'] + doc['roadCode'],
            'udrtYn' : doc['roadGroundCode'],
            'buldMnnm' : doc['roadMainCode'],
            'buldSlno' : doc['roadSubCode'],
        } 
        apt.DataReader(**inputs)
        longitude, latitudes = apt.getXY()
        colloction.update({'_id':doc['_id']}, { "$set": { 'longitude' : longitude,  "latitudes" : latitudes}}, multi=True)
        
    client.close()

if __name__ == "__main__":
    main()
    
