# Function to convert an array of numbers to an array of objects
def numbers_to_charcode_objects(numbers):
  result = []

  for num in numbers:
      # Converting a number to the corresponding character
      char_code = chr(num)
      result.append({str(num): char_code})

  return result

# Example usage
numbers = [100, 101, 102, 99, 97, 120]
print(numbers_to_charcode_objects(numbers))
