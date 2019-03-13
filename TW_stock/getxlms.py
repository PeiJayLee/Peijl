import urllib.request
import os

def set_time_C(times,name):
    path = os.path.join(os.getcwd(), name+'.csv')
    csv_file=("http://www.twse.com.tw/SBL/t13sa710?response=csv&startDate=%s&endDate=%s&stockNo=&tradeType=C" % (times,times))
    urllib.request.urlretrieve(csv_file, filename=path)

def set_time_N(times,name):
    path = os.path.join(os.getcwd(), name+'.csv')
    csv_file = ("http://www.twse.com.tw/SBL/t13sa710?response=csv&startDate=%s&endDate=%s&stockNo=&tradeType=N" % (times, times))
    urllib.request.urlretrieve(csv_file, filename=path)
