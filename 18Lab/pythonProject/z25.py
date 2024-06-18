def sum_less_than(list_a, value_k):

  sum_values = 0
  for element in list_a:
    if element < value_k:
      sum_values += element
  return sum_values
