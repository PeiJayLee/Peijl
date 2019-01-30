import pandas as pd
import datetime as dt
from heapq import nlargest
from TW_stock import gettwolist,getxlm,gettotalvalue,findrate,convertxl,Numbertrans,zeroone

# twolistint=gettwolist.aquiretwolist()
twolistint=gettwolist.ismellmagic()

today=dt.date.today()
now=dt.datetime.now()
if now.strftime('%A') == 'Monday':
    start = dt.datetime(today.year, today.month, today.day - 3)
    end = dt.datetime(today.year, today.month, today.day - 3)
else:
    start = dt.datetime(today.year, today.month, today.day-1)
    end = dt.datetime(today.year, today.month, today.day-1)

#以下是要給他們輸入日期的話的格式:
# start=input('Plese enter a  date (ex: 2019-01-25) : ')
# end=start

date_for_twse=(now.strftime('%Y')+now.strftime('%m')+now.strftime('%d'))

getxlm.set_time_C('SBL_C')
getxlm.set_time_N("SBL_N")
row=['Date','ID','Platform','Volume','Rate','Close','Return','Days','Changes']

wb_C=convertxl.create_your_workbook('SBL_C')
wb_C.save('SBL_CF.xlsx')

wb_N=convertxl.create_your_workbook('SBL_N')
ws_N = wb_N.active

#  下面是Negotiate(0.01%的尋找跟處理)
id_list_p=[]
volume_list_p=[]
for row in ws_N.iter_rows(min_row=2, min_col=5, max_row='', max_col=5):
    for cell in row:
        if cell.value == 0.01:
            po=(''.join([str(ord(ch) - 96) if ch.isalpha() else ch for ch in cell.column.lower()]))
            for coulm in ws_N.iter_cols(min_row=int(cell.row), min_col=2, max_row=int(cell.row), max_col=2):
                for x in coulm:
                    for s in str(x.value).split():
                        if s.isdigit():
                            id_list_p.append(s)

            for coulm in ws_N.iter_cols(min_row=int(cell.row), min_col=4, max_row=int(cell.row),max_col=4):
                 for x in coulm:
                    for s in str(x.value).split():
                         if s.isdigit():
                            volume_list_p.append(int(s))

for coo in ws_N.iter_cols(min_row=2, min_col=5, max_row='', max_col=5):
    for cell in coo:
        if cell.value == 0.01:
            ws_N.delete_rows(cell.row)

wb_N.save('SBL_NF.xlsx')

#做Negotiate(0.01%)的處理
dict = {"IDs": id_list_p,"Volumes": volume_list_p}
select_df = pd.DataFrame(dict)
grouped2=select_df.groupby(['IDs']).sum()
ggg=grouped2.to_dict()
aaa=ggg['Volumes']
five_largest=nlargest(len(aaa), aaa, key=aaa.get)
Nego_volume=[]
for qqq in five_largest:
    Nego_volume.append(aaa[qqq])

N_sid_list=findrate.sid_list_maker(aaa)
N_price_list=findrate.price_list_maker(N_sid_list,twolistint,start,end)
N_value_list=findrate.value_list_maker(N_price_list,Nego_volume)
N_value_topfive=sorted(N_value_list,reverse=True)[0:5]
N_valuetop_name=findrate.find_value_name(N_value_topfive,N_value_list,N_sid_list)

blankforl_NN=[]
for fufu in five_largest:
    blankforl_NN.append(aaa[fufu])
volume_NN_multiply=[]
for fefe in blankforl_NN:
    volume_NN_multiply.append(fefe*1000)
volume_NN_final=[]
for frfr in volume_NN_multiply:
    volume_NN_final.append(Numbertrans.millify(frfr))#這是0.01的volume

zero_one_N=0
for ghgh in N_value_topfive:
    zero_one_N+=int(ghgh)
zero_one_multi_N=zero_one_N*1000 #未更改的原始金額
Nego_value=Numbertrans.millify(zero_one_multi_N)
# Negotiate(0.01)的value

value_NN_multiply=[]
for wvwv in N_value_topfive:
    value_NN_multiply.append(wvwv * 1000)
value_NN_finals = []
for wvwvwv in value_NN_multiply:
    value_NN_finals.append(Numbertrans.millify(wvwvwv))

zero_check_Val_id=zeroone.check_valid_Negotiatezero(N_valuetop_name)
zero_check_Val=zeroone.check_value_Negotiatezero(value_NN_finals)
zero_check_Vol_id=zeroone.check_volid_Negotiatezero(five_largest)
zero_check_Vol=zeroone.check_volume_Negotiatezero(volume_NN_final)

#以下開始為處理正規競價_C和議借_N
#競價開始:
your_C_five_rates_Vol=[]
read_C=findrate.read_your_excel('SBL_CF')
C_V_pd=findrate.your_volume_pd(read_C)
five_largest_list_C=nlargest(5, C_V_pd, key=C_V_pd.get)
C_rate=findrate.read_your_excel_forrate('SBL_CF')
for yhyh in five_largest_list_C:
    C_rates=findrate.volume_largest_rate(C_rate,yhyh)
    C_total_rates=findrate.identification(C_rates)
    your_C_five_rates_Vol.append(C_total_rates)
five_largest_vol_sid_C=findrate.sid_list_maker(five_largest_list_C)

blankforl_C=[]
for ss in five_largest_list_C:
    blankforl_C.append(C_V_pd[ss])
volume_C_multiply=[]
for sss in blankforl_C:
    volume_C_multiply.append(sss*1000)
volume_C_final=[]
for ssss in volume_C_multiply:
    volume_C_final.append(Numbertrans.millify(ssss))

volume_list_C=findrate.volume_list_maker(C_V_pd)
sid_list_C=findrate.sid_list_maker(C_V_pd)
sid_list_C_ugly=findrate.sid_list_maker2(C_V_pd)
price_list_C=findrate.price_list_maker(sid_list_C,twolistint,start,end)
value_list_C=findrate.value_list_maker(price_list_C,volume_list_C)
value_topfive_C=sorted(value_list_C,reverse=True)[0:5]
valuetop_name_C=findrate.find_value_name(value_topfive_C,value_list_C,sid_list_C)
valuetop_name_C_ugly=findrate.find_value_name(value_topfive_C,value_list_C,sid_list_C_ugly)

valuetop_rates=[]
v_rates=findrate.volume_largest_rate_final(C_rate,valuetop_name_C_ugly)
for x in range(5):
    V_total_rates=findrate.identification2(v_rates,x)
    valuetop_rates.append(V_total_rates)

value_C_multiply=[]
for efef in value_topfive_C:
    value_C_multiply.append(efef * 1000)
value_C_final = []
for efefefef in value_C_multiply:
    value_C_final.append(Numbertrans.millify(efefefef))

#議借開始:
your_N_five_rates_V=[]
read_N=findrate.read_your_excel('SBL_NF')
N_V_pd=findrate.your_volume_pd(read_N)
five_largest_list_N=nlargest(5, N_V_pd, key=N_V_pd.get)
N_rate=findrate.read_your_excel_forrate('SBL_NF')
for x in five_largest_list_N:
    N_rates=findrate.volume_largest_rate(N_rate,x)
    N_total_rates=findrate.identification(N_rates)
    your_N_five_rates_V.append(N_total_rates)

five_largest_vol_sid_N=findrate.sid_list_maker(five_largest_list_N)

blankforl_N=[]
for tyty in five_largest_list_N:
    blankforl_N.append(N_V_pd[tyty])
volume_N_multiply=[]
for vyvy in blankforl_N:
    volume_N_multiply.append(vyvy*1000)
volume_N_final=[]
for opop in volume_N_multiply:
    volume_N_final.append(Numbertrans.millify(opop))

volume_list_N=findrate.volume_list_maker(N_V_pd)
sid_list_N=findrate.sid_list_maker(N_V_pd)
sid_list_N_ugly=findrate.sid_list_maker2(N_V_pd)
price_list_N=findrate.price_list_maker(sid_list_N,twolistint,start,end)
value_list_N=findrate.value_list_maker(price_list_N,volume_list_N)
value_topfive_N=sorted(value_list_N,reverse=True)[0:5]
valuetop_name_N=findrate.find_value_name(value_topfive_N,value_list_N,sid_list_N)
valuetop_name_N_ugly=findrate.find_value_name(value_topfive_N,value_list_N,sid_list_N_ugly)

# valuetop_rates_N=[]
# v_rates_N=findrate.volume_largest_rate2(N_rate,valuetop_name_N_ugly)
# V_total_rates_N=findrate.identification(v_rates_N)
# valuetop_rates_N.append(V_total_rates_N)

valuetop_rates_N=[]
v_rates_N=findrate.volume_largest_rate_final(N_rate,valuetop_name_N_ugly)
for qqa in range(5):
    V_total_rates_N=findrate.identification2(v_rates_N,qqa)
    valuetop_rates_N.append(V_total_rates_N)

value_N_multiply=[]
for uiui in value_topfive_N:
    value_N_multiply.append(uiui * 1000)
value_N_final = []
for uiuiui in value_N_multiply:
    value_N_final.append(Numbertrans.millify(uiuiui))

t_site=('http://www.twse.com.tw/SBL/t13sa710?response=json&startDate='+date_for_twse+'&endDate='+date_for_twse+'&stockNo=&tradeType=&_=1547881611266')
c_site=('http://www.twse.com.tw/SBL/t13sa710?response=json&startDate='+date_for_twse+'&endDate='+date_for_twse+'&stockNo=&tradeType=C&_=1547863612558')
n_site=('http://www.twse.com.tw/SBL/t13sa710?response=json&startDate='+date_for_twse+'&endDate='+date_for_twse+'&stockNo=&tradeType=N&_=1547863612558')

response_json_C=gettotalvalue.get_page_response(c_site)
Total_competetive=gettotalvalue.get_page_totalvalue(response_json_C)

response_json_N=gettotalvalue.get_page_response(n_site)
Total_negotiate=gettotalvalue.get_page_totalvalue(response_json_N)

response_json_T=gettotalvalue.get_page_response(t_site)
Total_shapes=gettotalvalue.get_total_shapes(response_json_T)
Total_values=gettotalvalue.get_page_totalvalue(response_json_T)


with open('SBL.txt',mode='w', encoding='utf-8') as file:
    file.write('***Today\'s TSE Daily Transaction Brief***\n'
               '-------------------------------------------------------------------------------------------------\n'
               'Total Value: NT$'+Total_values+'\n -Competitive: NT$'+Total_competetive+'\n -Negotiate (0.01%): NT$'+Nego_value+'\n -Negotiate (Non 0.01%): NT$'+Total_negotiate+'\nTotal Shapes:'+Total_shapes+'\n'
               '-------------------------------------------------------------------------------------------------\n'
               'Competitive Top 5 names\nBy Val: 1)'+valuetop_name_C[0]+'TT - NT$ '+str(value_C_final[0])+'('+valuetop_rates[0]+'%) 2)'+valuetop_name_C[1]+' TT- NT$'+str(value_C_final[1])+' ('+valuetop_rates[1]+'%) 3)'+valuetop_name_C[2]+'TT - NT$'+str(value_C_final[2])+' ('+valuetop_rates[2]+'%) 4)'+valuetop_name_C[3]+'TT - NT$'+str(value_C_final[3])+'('+valuetop_rates[3]+'%) 5)'+valuetop_name_C[4]+'TT - NT$'+str(value_C_final[4])+'('+valuetop_rates[4]+'%)\n '
               'By Vol: 1)'+five_largest_vol_sid_C[0]+'TT - '+volume_C_final[0]+' shs ('+your_C_five_rates_Vol[0]+'%)  2)'+five_largest_vol_sid_C[1]+'TT -'+volume_C_final[1]+' shs ('+your_C_five_rates_Vol[1]+'%)  3)'+five_largest_vol_sid_C[2]+'TT - '+volume_C_final[2]+' shs ('+your_C_five_rates_Vol[2]+'%)  4)'+five_largest_vol_sid_C[3]+'TT - '+volume_C_final[3]+' shs ('+your_C_five_rates_Vol[3]+'%)  5)'+five_largest_vol_sid_C[4]+'TT - '+volume_C_final[4]+' shs ('+your_C_five_rates_Vol[4]+'%)\n'
               '-------------------------------------------------------------------------------------------------\n'
               'Negotiate (0.01%) Top 5 names by value:\nBy Val:'+zero_check_Val_id+zero_check_Val+'\nBy Vol:'+zero_check_Vol_id+zero_check_Vol+'\n'
               '-------------------------------------------------------------------------------------------------\n'
               'Negotiate (none 0.01%) Top 5 names by value:\nBy Val: 1)'+valuetop_name_N[0]+'TT - NT$'+str(value_N_final[0])+'('+valuetop_rates_N[0]+'%) 2)'+valuetop_name_N[1]+'TT - NT$'+str(value_N_final[1])+'('+valuetop_rates_N[1]+'%) 3)'+valuetop_name_N[2]+'TT - NT$'+str(value_N_final[2])+'('+valuetop_rates_N[2]+'%) 4)'+valuetop_name_N[3]+'TT - NT$'+str(value_N_final[3])+'('+valuetop_rates_N[3]+'%) 5)'+valuetop_name_N[4]+'TT - NT$'+str(value_N_final[4])+'('+valuetop_rates_N[4]+'%) \n'
               'By Vol: 1)'+five_largest_vol_sid_N[0]+'TT -'+volume_N_final[0]+' shs ('+your_N_five_rates_V[0]+'%)  2)'+five_largest_vol_sid_N[1]+'TT -'+volume_N_final[1]+' shs ('+your_N_five_rates_V[1]+'%)  3)'+five_largest_vol_sid_N[2]+'TT -'+volume_N_final[2]+' shs ('+your_N_five_rates_V[2]+'%)  4)'+five_largest_vol_sid_N[3]+'TT -'+volume_N_final[3]+' shs ('+your_N_five_rates_V[3]+'%)  5)'+five_largest_vol_sid_N[4]+'TT -'+volume_N_final[4]+' shs ('+your_N_five_rates_V[4]+'%)  ')
