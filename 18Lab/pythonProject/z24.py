def count_greater_than(list_a, value_k):

  count = 0
  for element in list_a:
    if element > value_k:
      count += 1
  return count
