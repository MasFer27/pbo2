#NAMA : FERLI
#NIM     : 210511140
#KELAS: TI21 D

from functools import wraps

def calculate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Menghitung Berat Badan Ideal (BMI)")
        return func(*args, **kwargs)
    return wrapper

@calculate
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"

weight = float(input("Masukkan berat badan (kg): "))
height = float(input("Masukkan tinggi badan (m): "))

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

print("BMI Anda:", bmi)
print("Kategori BMI:", category)
