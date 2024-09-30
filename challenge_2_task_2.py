# Challenge 2 #
# Task 2 #
def reverse_name(name):
  return name[::-1]
# Method to intersperse a name #
def intersperse_name(reversed_name, surname):
  interspersed_name = ''.join(a + b for a, b in zip(reversed_name, surname))
  interspersed_name += reversed_name[len(surname):] + surname[len(reversed_name):]
  return interspersed_name
# Method to format the name as desired #
def format_name(intersperse_name):
  mid = len(intersperse_name) // 2
  first_half = intersperse_name[:mid].capitalize()
  second_half = intersperse_name[mid:].capitalize()
  return f"{first_half} {second_half}"
# Asking for the first name #
first_name = input("What is your name? ")
# Using the reverse name method to reverse the name #
reversed_first_name = reverse_name(first_name)
# Outputting the reversed name #
print(reversed_first_name)
# Asking for the surname #
surname = input("What is your surname? ")
# Interspersing the reversed first name with the surname as desired #
interspersed_name = intersperse_name(reversed_first_name, surname)
# Outputting the interspersed name #
print(interspersed_name)
# Using the method for formatting a name with the interspersed name #
formatted_name = format_name(interspersed_name)
# Outputting it
print("Your formatted name is:", formatted_name)
