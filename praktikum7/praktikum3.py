#NAMA : FERLI
#NIM     : 210511140
#KELAS: TI21 D

from functools import wraps
import math

def calculate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Menghitung volume dan luas permukaan kerucut")
        return func(*args, **kwargs)
    return wrapper

@calculate
def calculate_cone(radius, height):
    volume = (1 / 3) * math.pi * radius ** 2 * height
    surface_area = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
    return volume, surface_area

radius = float(input("Masukkan jari-jari kerucut: "))
height = float(input("Masukkan tinggi kerucut: "))
volume, surface_area = calculate_cone(radius, height)
print("Volume Kerucut:", volume)
print("Luas Permukaan Kerucut:", surface_area)
