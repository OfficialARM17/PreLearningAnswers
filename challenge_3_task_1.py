# Challenge 3 #
# Task 1 #
def ask_user_for_number():
  while True:
      user_input = input("Please enter a number: ")
      if user_input.isdigit():
          return int(user_input)
      else:
          print("Invalid input. Please enter a valid number.")
def sum_of_numbers():
  n = ask_user_for_number()
  total_sum = sum(range(1, n + 1))
  print(f"The sum of numbers from 1 to {n} is {total_sum}.")
def sum_of_multiples_of_3_or_5():
  n = ask_user_for_number()
  total_sum = sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)
  print(f"The sum of multiples of 3 or 5 from 1 to {n} is {total_sum}.")
def sum_or_product_of_numbers():
  n = ask_user_for_number()
  while True:
      choice = input("Press '1' to compute the sum or '2' to compute the product: ").lower()
      if choice == '1':
          total_sum = sum(range(1, n + 1))
          print(f"The sum of numbers from 1 to {n} is {total_sum}.")
          break
      elif choice == '2':
          product = 1
          for i in range(1, n + 1):
              product *= i
          print(f"The product of numbers from 1 to {n} is {product}.")
          break
      else:
          print("Invalid choice. Please enter 'sum' or 'product'.")
def main_menu():
  while True:
      print("\nSelect an operation:")
      print("1. Compute the sum of numbers from 1 to n")
      print("2. Compute the sum of multiples of 3 or 5 from 1 to n")
      print("3. Compute the sum or product of numbers from 1 to n")
      print("4. Exit")
      choice = input("Enter your choice (1-4): ")
      if choice == '1':
          sum_of_numbers()
      elif choice == '2':
          sum_of_multiples_of_3_or_5()
      elif choice == '3':
          sum_or_product_of_numbers()
      elif choice == '4':
          print("Goodbye!")
          break
      else:
          print("Invalid choice. Please select a valid option.")
main_menu()
