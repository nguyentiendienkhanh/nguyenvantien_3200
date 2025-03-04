def dem_so_lan_xuat_hien(lst):
    cout_dict = {}
    for num in lst:
        if num in cout_dict:
            cout_dict[num] += 1
        else:
            cout_dict[num] = 1
    return cout_dict
input_string = input("Nhập danh sách các từừ, cách nhau bằng dấu cách: ")
word_list = input_string.split(' ')
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của mỗi từ: ", so_lan_xuat_hien)