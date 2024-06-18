def cube(x):
    return x ** 3

numbers = input("Введите список чисел через пробел: ").split()
numbers = list(map(int, numbers))

negative_numbers = filter(lambda x: x < 0, numbers)
sum_cube_negative = sum(map(cube, negative_numbers))

print("Сумма кубов отрицательных чисел:", sum_cube_negative)
