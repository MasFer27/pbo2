#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    # Potongan kode yang mungkin menimbulkan TabError
    if True:
        print("Halo")
    else:
        print("Dunia")
except TabError:
    # Tangani kesalahan di sini
    print("Kesalahan: jangan campur spasi dan tab untuk menentukan blok kode")
