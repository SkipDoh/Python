import z24

def main():

  list_a = [1, 5, 3, 8, 2, 7, 4]
  value_k = 4

  count = z24.count_greater_than(list_a, value_k)
  print(f"В списке {list_a} количество элементов, превышающих {value_k}: {count}")

if __name__ == "__main__":
  main()
