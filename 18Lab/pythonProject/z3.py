def sum_of_digits(number):

  sum_digits = 0
  while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10
  return sum_digits

def find_number_with_max_digit_sum(numbers):

  if not numbers:
    return None

  max_sum = sum_of_digits(numbers[0])
  max_number = numbers[0]
  for number in numbers:
    current_sum = sum_of_digits(number)
    if current_sum > max_sum:
      max_sum = current_sum
      max_number = number
  return max_number