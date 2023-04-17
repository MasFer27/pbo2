#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    # membuat string dengan karakter unicode yang tidak dapat diterjemahkan
    s = "안녕하세요".encode("ascii")
except UnicodeTranslateError as e:
    print("Error:", e)
