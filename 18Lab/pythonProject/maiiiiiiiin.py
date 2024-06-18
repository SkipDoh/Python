import z27

def main():

  list_a = [1, 2, 3, 4, 5]
  index_k = 2

  list_a = z27.remove_by_index(list_a, index_k)
  print(f"Список A (после удаления элемента с индексом {index_k}): {list_a}")

if __name__ == "__main__":
  main()
