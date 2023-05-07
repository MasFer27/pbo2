#NAMA : FERLI
#NIM     : 210511140
#KELAS: TI21 D

from functools import wraps
import math

def calculate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Menghitung volume dan luas permukaan tabung")
        return func(*args, **kwargs)
    return wrapper

@calculate
def calculate_cylinder(radius, height):
    volume = math.pi * radius ** 2 * height
    surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)
    return volume, surface_area

radius = float(input("Masukkan jari-jari tabung: "))
height = float(input("Masukkan tinggi tabung: "))
volume, surface_area = calculate_cylinder(radius, height)
print("Volume Tabung:", volume)
print("Luas Permukaan Tabung:", surface_area)
