
import json
import xmltodict
import pandas as pd
from os import path
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request

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
            })

        request = Request(self.URL + queryParams + self.service_key)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode('utf8')
        json_data = xmltodict.parse(response_body)

        return json_data


def main():
    abs_path = path.dirname(path.realpath(__file__))
    with open(path.join(abs_path, "apt_unique_info.json"), "r", encoding="utf-8") as r_file: 
            apt_info = json.load(r_file)

    apt = AptLocationAPI("devU01TX0FVVEgyMDIwMDIwNjIzMDE1MjEwOTQ0NzQ=")
    output = []
    for _, info in apt_info.items():
        inputs = {
            'admCd' : info['road_city_code'] + info['law_town_code'],
            'rnMgtSn' : info['road_city_code'] + info['road_code'],
            'udrtYn' : info['road_ground_code'],
            'buldMnnm' : info['road_main_code'],
            'buldSlno' : info['road_sub_code'],
        } 
        json_data = apt.DataReader(**inputs)
        output.append(json_data)

    with open("apt_location.json", "w", encoding="utf-8") as make_file:
        json.dump(output, make_file, ensure_ascii=False, indent="\t")

if __name__ == "__main__":
    main()
    