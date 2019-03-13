
def check_volume_Negotiatezero(list):
    if list == []:
        return('None')
    else:
        return (list[:len(list)])

def check_volid_Negotiatezero(list2):
    if list2 == []:
        return ''
    else:
        return (list2[:len(list2)])

def check_value_Negotiatezero(list3):
    if list3 == []:
        return('None')
    else:
        return (list3[:len(list3)])

def check_valid_Negotiatezero(list4):
    if list4 == []:
        return ''
    else:
        return (list4[:len(list4)])

def KaiXuan(v_id_list,v_v_list):
    if v_id_list == '':
        return('None')
    else:
        if len(v_id_list)>1:
            return '1)'+v_id_list[0]+'TT - NT$'+v_v_list[0]+' 2)'+v_id_list[1]+'TT - NT$'+v_v_list[1]
        elif len(v_id_list)>2:
            return '1)'+v_id_list[0]+'TT - NT$'+v_v_list[0]+' 2)'+v_id_list[1]+'TT - NT$'+v_v_list[1]+' 3)'+v_id_list[2]+'TT - NT$'+v_v_list[2]
        elif len(v_id_list)>3:
            return '1)'+v_id_list[0]+'TT - NT$'+v_v_list[0]+' 2)'+v_id_list[1]+'TT - NT$'+v_v_list[1]+' 3)'+v_id_list[2]+'TT - NT$'+v_v_list[2]+' 4)'+v_id_list[3]+'TT - NT$'+v_v_list[3]
        elif len(v_id_list) > 4:
            return '1)'+v_id_list[0]+'TT - NT$'+v_v_list[0]+' 2)'+v_id_list[1]+'TT - NT$'+v_v_list[1]+' 3)'+v_id_list[2]+'TT - NT$'+v_v_list[2]+' 4)'+v_id_list[3]+'TT - NT$'+v_v_list[3]+' 5)'+v_id_list[4]+'TT - NT$'+v_v_list[4]
        else:
            return '1)'+v_id_list[0]+'TT - NT$'+v_v_list[0]

def Babykaixuan(vol_id_list,vol_vol_list):
    if vol_id_list == '':
        return('None')
    else:
        if len(vol_id_list)>1:
            return '1)'+vol_id_list[0]+'TT - '+vol_vol_list[0]+' shs 2)'+vol_id_list[1]+'TT - '+vol_vol_list[1]+' shs'
        elif len(vol_id_list)>2:
            return '1)'+vol_id_list[0]+'TT - '+vol_vol_list[0]+' shs 2)'+vol_id_list[1]+'TT - '+vol_vol_list[1]+' shs 3)'+vol_id_list[2]+'TT - '+vol_vol_list[2]+' shs'
        elif len(vol_id_list)>3:
            return '1)'+vol_id_list[0]+'TT - '+vol_vol_list[0]+' shs 2)'+vol_id_list[1]+'TT - '+vol_vol_list[1]+' shs 3)'+vol_id_list[2]+'TT - '+vol_vol_list[2]+' shs 4)'+vol_id_list[3]+'TT - '+vol_vol_list[3]+' shs'
        elif len(vol_id_list) > 4:
            return '1)'+vol_id_list[0]+'TT - '+vol_vol_list[0]+' shs 2)'+vol_id_list[1]+'TT - '+vol_vol_list[1]+' shs 3)'+vol_id_list[2]+'TT - '+vol_vol_list[2]+' shs 4)'+vol_id_list[3]+'TT - '+vol_vol_list[3]+' shs 5)'+vol_id_list[4]+'TT - '+vol_vol_list[4]+' shs'
        else:
            return '1)'+vol_id_list[0]+'TT - '+vol_vol_list[0]+' shs'
