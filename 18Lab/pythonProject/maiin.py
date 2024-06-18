import z2

def main():

  list_a = [1, 2, 3, 4, 3, 5, 6, 3]
  value_k = 3

  list_b = z2.filter_list(list_a, value_k)
  print(f"Список A: {list_a}")
  print(f"Список B (без элементов, равных {value_k}): {list_b}")

if __name__ == "__main__":
  main()
