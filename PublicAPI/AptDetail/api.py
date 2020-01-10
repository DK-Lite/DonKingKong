
import json
import xmltodict
import pandas as pd
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request

class AptDetailReader:

    URL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    NUM_OF_ROWS = "10000"
    def __init__(self, service_key):
        self.service_key = service_key
    
    def DataReader(self, LAWD_CD, DEAL_YMD):

        queryParams = '?' + urlencode({ \
            quote_plus('LAWD_CD') : LAWD_CD,
            quote_plus('DEAL_YMD') : DEAL_YMD,
            quote_plus('numOfRows') : self.NUM_OF_ROWS,
            })

        request = Request(self.URL + queryParams + self.service_key)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read().decode('utf8')
        
        return self.__json2pd(xmltodict.parse(response_body))

    def __json2pd(self, json_data):

        items = json_data['response']['body']['items']
        if items is None: 
            return pd.DataFrame()

        datas = items['item']
        output = pd.DataFrame(columns=datas[0].keys())
        
        #pd.concat([ pd.DataFrame(data, columns=datas[0].keys()) for data in datas ], ignore_index=True)
        
        for data in datas :
            output = output.append(data, ignore_index=True)

        return output


def main():
    apt = AptDetailReader("&ServiceKey=aKVcsSF8UlpRkppSsPS38IZO8UZ87fNBzMTtrrWtoadmn7ySBos%2BX8AOc6M%2F47Temd2cIbpl4%2BFxq%2Btu0KoKWA%3D%3D")
    df_data = apt.DataReader("41135", "201911")
    print(df_data.head())

if __name__ == "__main__":
    main()
    