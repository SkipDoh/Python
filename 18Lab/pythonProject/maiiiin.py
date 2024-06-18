import z23

def main():

  list_a = []
  value_k = 5
  num_elements = int(input("Сколько элементов списка следует заполнить? "))

  z23.fill_list(list_a, value_k, num_elements)
  print(f"Список A (заполненный значением {value_k}): {list_a}")

if __name__ == "__main__":
  main()
