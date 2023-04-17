#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    x = 1.0 / 0.0
except ZeroDivisionError:
    print("Pembagian dengan nol tidak dapat dilakukan")
except FloatingPointError:
    print("Operasi floating point tidak valid")
