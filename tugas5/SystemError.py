#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    # Potongan kode yang mungkin menimbulkan SystemError
    a = 10
    b = 0
    c = a / b
except SystemError:
    # Tangani kesalahan di sini
    print("Kesalahan sistem terdeteksi. Mohon coba lagi nanti.")
