import z28

def main():

  list_a = [1, 2, 3, 4, 3, 5, 6, 3]
  value_k = 3
  value_m = 0

  z28.replace_elements(list_a, value_k, value_m)
  print(f"Список A (после замены элементов, отличных от {value_k}, на {value_m}): {list_a}")

if __name__ == "__main__":
  main()
