#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    num_list = [1, 2, 3, 4, 5]
    print(num_list[10])
except IndexError:
    print("Indeks di luar jangkauan.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
