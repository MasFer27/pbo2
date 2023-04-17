#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

list_angka = [3,4,5] 
try: 
    value = list_angka[9] 
except IndexError: 
    print("Index yang diminta melebihi jumlah elemen dalam list!")