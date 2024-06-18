import z25

def main():
 
  list_a = [1, 5, 3, 8, 2, 7, 4]
  value_k = 5

  sum_values = z25.sum_less_than(list_a, value_k)
  print(f"Сумма элементов списка {list_a}, меньших {value_k}: {sum_values}")

if __name__ == "__main__":
  main()
