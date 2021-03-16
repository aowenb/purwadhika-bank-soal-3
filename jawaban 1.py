def remove(x):
    return x.replace(' ','').upper()
    
while True:
    try:
        x = str(input('Masukkan Sebuah Kalimat : '))
    except ValueError:
        print('masukkan sebuah inputan')
        continue
    if len(x) > 200:
        print('Batas Karakter Maksimal Hanya 200')
        break
    else:
        print('*',remove(x),'*')
        break