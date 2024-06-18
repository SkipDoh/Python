def get_numbers():
  """Получает список чисел от пользователя."""
  numbers_str = input("Введите числа через пробел: ")
  return [int(num) for num in numbers_str.split()]

def is_three_digit_even_divisible_by_6(number):
  """Проверяет, является ли число трехзначным четным и делимым на 6."""
  return 100 <= number <= 999 and number % 2 == 0 and number % 6 == 0

def main():
  """Основная функция программы."""
  numbers = get_numbers()
  filtered_numbers = filter(is_three_digit_even_divisible_by_6, numbers)
  print("Трехзначные четные числа, делимые на 6:", list(filtered_numbers))

if __name__ == "__main__":
  main()

