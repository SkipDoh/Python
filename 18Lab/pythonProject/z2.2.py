def insert_sorted(list_a, value_k):
  for i in range(len(list_a)):
    if value_k <= list_a[i]:
      list_a.insert(i, value_k)
      return list_a
  list_a.append(value_k) 
  return list_a
