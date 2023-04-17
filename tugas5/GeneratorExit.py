#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

def my_generator():
    yield 1
    yield 2
    yield 3

try:
    gen = my_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("Generator sudah selesai menghasilkan nilai")
except GeneratorExit:
    print("Generator dihentikan sebelum selesai menghasilkan nilai")
