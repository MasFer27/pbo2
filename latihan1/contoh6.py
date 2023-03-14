class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(23, 25)) # Output: 48
print(Kalkulator.subtract(33, 21)) # Output: 12
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(3, 15)) # Output: 45
print(Kalkulator.divide(25, 5)) # Output: 5.0