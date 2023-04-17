#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

import sys

def recursive_function(x):
    try:
        if x == 0:
            return 1
        else:
            return x * recursive_function(x - 1)
    except RecursionError:
        print("Terjadi kesalahan rekursi. Coba gunakan nilai yang lebih kecil.")

try:
    result = recursive_function(10000)
    print(result)
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
