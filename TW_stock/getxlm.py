from time import strftime
import urllib.request
import os

def set_time_C(name):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    tm = strftime("%B")
    wm = "0" + str(months.index(tm) + 1)
    wy = strftime("%Y")
    wd = strftime("%d")
    ct = str(wy) + str(wm) + str(wd)
    path = os.path.join(os.getcwd(), name+'.csv')
    csv_file=("http://www.twse.com.tw/SBL/t13sa710?response=csv&startDate=%s&endDate=%s&stockNo=&tradeType=C" % (ct,ct))
    urllib.request.urlretrieve(csv_file, filename=path)

def set_time_N(name):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    tm = strftime("%B")
    wm = "0" + str(months.index(tm) + 1)
    wy = strftime("%Y")
    wd = strftime("%d")
    ct = str(wy) + str(wm) + str(wd)
    path = os.path.join(os.getcwd(), name+'.csv')
    csv_file = ("http://www.twse.com.tw/SBL/t13sa710?response=csv&startDate=%s&endDate=%s&stockNo=&tradeType=N" % (ct, ct))
    urllib.request.urlretrieve(csv_file, filename=path)

