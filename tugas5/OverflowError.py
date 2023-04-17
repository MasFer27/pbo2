#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

import math

try:
    result = math.exp(1000)
except OverflowError:
    print("Hasil perhitungan melebihi batas nilai yang dapat diwakili oleh tipe data float")
