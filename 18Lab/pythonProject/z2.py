def filter_list(list_a, value_k):

  list_b = []
  for element in list_a:
    if element != value_k:
      list_b.append(element)
  return list_b
