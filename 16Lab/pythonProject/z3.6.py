def get_odd_divisible_by_eleven(numbers):
    return [num for num in numbers if num % 2 != 0 and num % 11 == 0]

numbers = input("Введите числа через пробел: ").split()
numbers = [int(num) for num in numbers]

result = get_odd_divisible_by_eleven(numbers)
print("Числа, нечетные и делящиеся на 11:", result)