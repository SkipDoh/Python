from functools import reduce

def is_positive(num):
    return num > 0

def main():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    positive_numbers = list(filter(is_positive, numbers))

    sum_of_squares = reduce(lambda a, b: a + b**2, positive_numbers, 0)

    print("Сумма квадратов положительных чисел из списка:", sum_of_squares)

if __name__ == "__main__":
    main()
