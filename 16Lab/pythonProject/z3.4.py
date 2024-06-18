def get_divisible_by_seventeen(numbers):
    return [num for num in numbers if num % 17 == 0]

numbers = input("Введите числа через пробел: ").split()
numbers = [int(num) for num in numbers]

result = get_divisible_by_seventeen(numbers)
print("Числа, делящиеся на 17:", result)
