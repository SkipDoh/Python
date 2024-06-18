def say_hello(name):

  print(f"Привет, {name}!")

def calculate_average(numbers):

  if not numbers:
    return 0
  return sum(numbers) / len(numbers)
