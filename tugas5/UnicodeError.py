#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    # Potongan kode yang mungkin menimbulkan UnicodeError
    data = "Contoh teks dengan karakter non-ASCII: àáâ"
    encoded_data = data.encode('ascii')
    decoded_data = encoded_data.decode('utf-8')
    print(decoded_data)
except UnicodeError:
    # Tangani kesalahan di sini
    print("Kesalahan: terjadi kesalahan Unicode saat mengolah data")
