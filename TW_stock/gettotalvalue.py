import sys, json
import urllib.request as ur
from urllib.parse import urlencode
import requests
from TW_stock import Numbertrans

t_site=('http://www.twse.com.tw/SBL/t13sa710?response=json&startDate=20190118&endDate=20190118&stockNo=&tradeType=&_=1547881611266')
c_site=('http://www.twse.com.tw/SBL/t13sa710?response=json&startDate=20190118&endDate=20190118&stockNo=&tradeType=C&_=1547863612558')
n_site=('http://www.twse.com.tw/SBL/t13sa710?response=json&startDate=20190118&endDate=20190118&stockNo=&tradeType=N&_=1547863612558')


def get_page_response(result):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    try:
        response = requests.get(result, headers=headers)
        if response.status_code == 200:
            return response
    except:
        return None
    # try:
    #     response=requests.get(result,headers=headers)
    #     if response.status_code == '200':
    #         return response.text
    #     return None
    # except:
    #     return None


def get_page_totalvalue(responses):
    resultJson = json.loads(responses.text)
    total_value=resultJson.get('notes')
    x=total_value[-1]
    a=list(filter(str.isdigit, x))
    for dada in range(2):
        a.pop(-1)
    b=int(''.join(a))
    return Numbertrans.millify(b)

def get_total_shapes(responses):
    resultJson = json.loads(responses.text)
    total_value = resultJson.get('notes')
    x = total_value[0]
    a = list(filter(str.isdigit, x))
    return (''.join(a))


# response_json=get_page_response(t_site)
# get_total_shapes(response_json)

