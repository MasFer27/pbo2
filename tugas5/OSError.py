#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

import os

try:
    os.remove("file_yang_tidak_ada.txt")
except OSError as error:
    print(f"Tidak dapat menghapus file: {error}")
