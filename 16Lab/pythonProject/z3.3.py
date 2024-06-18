numbers = input("Введите список чисел через пробел: ").split()
numbers = list(map(int, numbers))

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print("Четные числа из списка:", list(even_numbers))
