def is_three_digit_and_divisible_by_8(num):
    return num >= 100 and num <= 999 and num % 8 == 0

def cube(n):
    return n ** 3

numbers = input("Введите числа через пробел: ").split()
numbers = list(map(int, numbers))

filtered_numbers = list(filter(is_three_digit_and_divisible_by_8, numbers))
cubes = list(map(cube, filtered_numbers))

sum_cubes = sum(cubes)

print(f"Сумма кубов всех трехзначных чисел, делящихся на 8: {sum_cubes}")
