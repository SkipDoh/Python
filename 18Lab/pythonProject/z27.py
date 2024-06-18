def remove_by_index(list_a, index_k):

  if 0 <= index_k < len(list_a):
    del list_a[index_k]
  return list_a