# Challenge 2 #
# Task 2 #
def reverse_name(name):
  return name[::-1]

def intersperse_name(reversed_name, surname):
  interspersed = ''.join(a + b for a, b in zip(reversed_name, surname))
  interspersed += reversed_name[len(surname):] + surname[len(reversed_name):]
  return interspersed

def format_name(intersperse_name):
  mid = len(intersperse_name) // 2
  first_half = intersperse_name[:mid].capitalize()
  second_half = intersperse_name[mid:].capitalize()
  return f"{first_half} {second_half}"

first_name = input("What is your name? ")
reversed_first_name = reverse_name(first_name)
print(reversed_first_name)
surname = input("What is your surname? ")
interspersed_name = intersperse_name(reversed_first_name, surname)
print(interspersed_name)
formatted_name = format_name(interspersed_name)
print("Your formatted name is:", formatted_name)
