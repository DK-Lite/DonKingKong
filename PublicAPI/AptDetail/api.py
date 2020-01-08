
import json
import xmltodict
import pandas as pd
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request

class AptDetailReader:

    URL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'

    def __init__(self, service_key):
        self.service_key = service_key
    
    def DataReader(self, LAWD_CD, DEAL_YMD):

        queryParams = '?' + urlencode({ \
            quote_plus('LAWD_CD') : LAWD_CD,
            quote_plus('DEAL_YMD') : DEAL_YMD,
            })
        request = Request(url + queryParams + self.service_key)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode('utf8')
        
        return __json2pd(xmltodict.parse(response_body))

    def __json2pd(self, json_data):
        pass

def main():
    apt = AptDetailReader("&ServiceKey=aKVcsSF8UlpRkppSsPS38IZO8UZ87fNBzMTtrrWtoadmn7ySBos%2BX8AOc6M%2F47Temd2cIbpl4%2BFxq%2Btu0KoKWA%3D%3D")
    df_data = apt.DataReader("41135", "201911")

if __name__ == "__main__":
    main()
    