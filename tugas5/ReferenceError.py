#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    x = some_variable_that_does_not_exist
except NameError:
    print("Terjadi kesalahan referensi. Pastikan variabel sudah didefinisikan.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
