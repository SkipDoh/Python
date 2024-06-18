def find_max_element(list_a):

  if not list_a:
    return None

  max_element = list_a[0]
  for element in list_a:
    if element > max_element:
      max_element = element
  return max_element

def count_max_elements(list_a):

  max_element = find_max_element(list_a)
  if max_element is None:
    return 0

  count = 0
  for element in list_a:
    if element == max_element:
      count += 1
  return count