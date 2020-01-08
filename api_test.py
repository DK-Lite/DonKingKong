import json
import xmltodict
#from urllib import urlencode, quote_plus, Request
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
service_key = "&ServiceKey=aKVcsSF8UlpRkppSsPS38IZO8UZ87fNBzMTtrrWtoadmn7ySBos%2BX8AOc6M%2F47Temd2cIbpl4%2BFxq%2Btu0KoKWA%3D%3D"

with open('./data/output.txt', 'r') as r_file:
    lines = r_file.readlines()


for line in lines:
    LAWD_CD = line[0:-1]
    DEAL_YMD = "201912"
    w_filename = "./data/{}.json".format(DEAL_YMD+"_"+LAWD_CD)
    
    print(LAWD_CD, DEAL_YMD)
    queryParams = '?' + urlencode({ \
        quote_plus('LAWD_CD') : LAWD_CD,
        quote_plus('DEAL_YMD') : DEAL_YMD,
        })
    request = Request(url + queryParams + service_key)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf8')

    with open(w_filename, "w", encoding="utf-8") as make_file:
        json.dump(xmltodict.parse(response_body), make_file, ensure_ascii=False, indent="\t")
    print("create file: " + w_filename)
    #with open(w_filename, "w", encoding="utf-8") as make_file:
    #    json.dump("[]", make_file, ensure_ascii=False, indent="\t")
