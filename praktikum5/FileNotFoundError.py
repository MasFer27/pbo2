#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File tidak ditemukan")
