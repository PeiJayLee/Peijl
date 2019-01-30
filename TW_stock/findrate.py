import pandas as pd
from heapq import nlargest
import pandas_datareader.data as web


def read_your_excel(name):
    return pd.read_excel(name+'.xlsx', encoding='utf-8', parse_dates=['Date'], dayfirst=True, index_col='Date')

def your_volume_pd(excel):
    gy = excel[['ID', 'Volume']]
    grouped2 = gy.groupby(['ID']).sum()
    ggg = grouped2.to_dict()
    findic = ggg['Volume']
    return findic

def read_your_excel_forrate(name):
    df2 = pd.read_excel(name+'.xlsx', encoding='utf-8', dayfirst=True)
    return df2[['ID','Rate']]

def volume_largest_rate(excel,list):
    five_largest_rate=[]
    idx = (excel['ID']== list)
    number = excel.loc[idx,'Rate']
    for x in number:
        five_largest_rate.append(x)
    return five_largest_rate

def identification(list):
    if max(list) == min(list):
        return str(max(list))
    else:
        return str(min(list))+'-'+str(max(list))

def identification2(list,num):
    if max(list[num]) == min(list[num]):
        return str(max(list[num]))
    else:
        return str(min(list[num]))+'-'+str(max(list[num]))

def volume_list_maker(dic):
    volume_list = []
    for x in dic:
        a = dic.get(x)
        volume_list.append(a)
    return volume_list

def sid_list_maker(dict):
    sid_list = []
    for x in dict:
        for s in x.split():
            if s.isdigit():
                sid = str(s)
                sid_list.append(sid)
    return sid_list

def price_list_maker(sidlist,twolistint,start,end):
    price_list = []
    for x in sidlist:
        if x not in twolistint:
            price = web.get_data_yahoo([x+'.TW'], start, end)
            nondemical = price['Close'].values
            afterprice = round(int(nondemical), 2)
            price_list.append(afterprice)
        else:
            price = web.get_data_yahoo([x+'.TWO'], start, end)
            nondemical = price['Close'].values
            afterprice = round(int(nondemical), 2)
            price_list.append(afterprice)
    return price_list

def value_list_maker(price_list,volume_list):
    value_list = []
    for x in range(len(price_list)):
        values = price_list[x] * volume_list[x]
        value_list.append(values)
    return value_list


def find_value_name(value_topfive, value_list,sid_list):
    valuetop_name = []
    for x in value_topfive:
        if value_topfive.count(x) > 1:
            double = value_list.index(x)
            corrname = sid_list[double]
            valuetop_name.append(corrname)
            sid_list.remove(corrname)
            sid_list.insert(double, 0)
            value_list.remove(x)
            value_list.insert(double, 0)
        else:
            valuepo = value_list.index(x)
            corrname = sid_list[valuepo]
            valuetop_name.append(corrname)
    return valuetop_name

# def volume_largest_rate2(excel,list):
#     individual_rate=[]
#     five_largest_rate=[]
#     for gg in list:
#         idx = (excel['ID']== gg)
#         number = excel.loc[idx,'Rate']
#         for x in number:
#             individual_rate.append(x)
#     five_largest_rate.append(individual_rate)
#     return five_largest_rate

def sid_list_maker2(dict):
    sid_list = []
    for x in dict:
        sid = x
        sid_list.append(sid)
    return sid_list


def volume_largest_rate_final(excel,id_list):
    littlegreen=[]
    sum = 0
    while sum < 5:
        idx = (excel['ID'] == id_list[sum])
        number = excel.loc[idx, 'Rate']
        littlegreen.append(list(number))
        sum += 1
    return littlegreen

