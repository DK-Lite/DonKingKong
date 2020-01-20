
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
        
        json_data = xmltodict.parse(response_body)
        items = json_data['response']['body']['items']
        if items is None:
            return None

        return items['item']
        
    # def DataReaderToJSON(self, LAWD_CD, DEAL_YMD):
    #     return self.DataReader(LAWD_CD, DEAL_YMD)

    # def DataReaderToDF(self, LAWD_CD, DEAL_YMD):
    #     json_data = self.DataReader(LAWD_CD, DEAL_YMD)
    #     return self.__json2pd(json_data)

    # def __json2pd(self, json_data):

    #     items = json_data['response']['body']['items']
    #     if items is None:
    #         return pd.DataFrame()

    #     datas = items['item']
    #     output = pd.DataFrame(columns=datas[0].keys())
    #     for data in datas :
    #         output = output.append(data, ignore_index=True)

    #     return output.copy()


def main():
    apt = AptDetailReader()
    json_data = apt.DataReader("41135", "201911")

    with open("output.json", "w", encoding="utf-8") as make_file:
        json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

if __name__ == "__main__":
    main()
    