import z3

def main():

  numbers = [123, 456, 789, 100, 555]

  max_number = z3.find_number_with_max_digit_sum(numbers)
  print(f"Число с максимальной суммой цифр в списке {numbers}: {max_number}")

if __name__ == "__main__":
  main()
