from functools import reduce

def is_single_digit(num):
    return num >= 0 and num < 10

def is_even(num):
    return num % 2 == 0

def main():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    filtered_numbers = list(filter(lambda x: is_single_digit(x) and is_even(x), numbers))

    squared_numbers = list(map(lambda x: x**2, filtered_numbers))

    result = reduce(lambda x, y: x * y, squared_numbers, 1)

    print("Произведение квадратов однозначных чисел, делящихся на 2:", result)

if __name__ == "__main__":
    main()
