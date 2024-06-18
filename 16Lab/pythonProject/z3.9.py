from functools import reduce

def is_two_digit_divisible_by_7(num):
    return len(str(num)) == 2 and num % 7 == 0

def main():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    two_digit_numbers_div_by_7 = list(filter(is_two_digit_divisible_by_7, numbers))

    sum_of_squares = reduce(lambda a, b: a + b**2, two_digit_numbers_div_by_7, 0)

    print("Сумма квадратов двузначных чисел, делящихся на 7:", sum_of_squares)

if __name__ == "__main__":
    main()
