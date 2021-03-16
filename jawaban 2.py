x = input('Masukkan Nomor HP : ')

def check_num(x):
    x_list = str(x)[:2]

    if len(x) > 13:
        return 'Nomor HP maksimal 13 Angka'
    elif x_list != '08':
        return 'Nomor HP harus dimulai dengan "08" '
    else:
        return x

print(check_num(x))