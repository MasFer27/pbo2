#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

def fungsi():
    try:
        # Potongan kode yang mungkin menimbulkan UnboundLocalError
        pesan = "Halo"
        print(pesan)
        pesan = pesan + " Dunia"
    except UnboundLocalError:
        # Tangani kesalahan di sini
        pesan = "Halo Dunia"
    print(pesan)

fungsi()
