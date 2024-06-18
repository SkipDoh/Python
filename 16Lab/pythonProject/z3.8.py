def is_odd(num):
    return num % 2 != 0

def main():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    odd_numbers = list(filter(is_odd, numbers))

    if odd_numbers:
        print("Нечетные числа из списка:", odd_numbers)
    else:
        print("Нечетных чисел в списке нет")

if __name__ == "__main__":
    main()
