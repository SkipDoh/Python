import my_utils

def main():

  my_utils.say_hello("Иван")

  numbers = [1, 2, 3, 4, 5]
  average = my_utils.calculate_average(numbers)
  print(f"Среднее значение: {average}")

if __name__ == "__main__":
  main()
