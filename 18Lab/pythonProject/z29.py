def find_max_element(list_a):

  if not list_a:
    return None  # Возвращает None, если список пустой

  max_element = list_a[0]
  for element in list_a:
    if element > max_element:
      max_element = element
  return max_element