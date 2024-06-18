import z22

def main():

  list_a = [1, 3, 5, 7, 9]
  value_k = 6

  list_a = z22.insert_sorted(list_a, value_k)
  print(f"Список A (после вставки {value_k}): {list_a}")

if __name__ == "__main__":
  main()
