import math

def L(x, y, z):
    return (math.cos(z) + math.cos(y) + math.cos(x)) * (math.cos(3 * z) + math.cos(3 * y) + math.cos(3 * x))

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))

result = L(x, y, z)
print("Значение выражения L = ", result)