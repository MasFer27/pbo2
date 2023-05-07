#NAMA : FERLI
#NIM     : 210511140
#KELAS: TI21 D

from functools import wraps

def calculate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Menghitung volume dan luas permukaan balok")
        return func(*args, **kwargs)
    return wrapper

@calculate
def calculate_cuboid(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)
    return volume, surface_area

length = float(input("Masukkan panjang balok: "))
width = float(input("Masukkan lebar balok: "))
height = float(input("Masukkan tinggi balok: "))
volume, surface_area = calculate_cuboid(length, width, height)
print("Volume Balok:", volume)
print("Luas Permukaan Balok:", surface_area)
