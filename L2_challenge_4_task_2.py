animals = [
  { "name": "Fluffy", "type": "dog" },
  { "name": "Parsley", "type": "dog" },
  { "name": "Ginger", "type": "cat" },
  { "name": "Biscuit", "type": "cat" },
  { "name": "Poppet", "type": "Cow" }  # Test case for invalid type
]
def say_hello_to_pets(pets):
  for pet in pets:
      hello_message = ""
      pet_name = pet["name"]  # Access the pet's name

      # Check the type of pet and generate appropriate message
      if pet["type"] == "dog":
          hello_message = "Woof"
      elif pet["type"] == "cat":
          hello_message = "Meow"
      else:
          # Raise an exception for any type other than "dog" or "cat"
          raise ValueError(f"Unknown animal type '{pet['type']}' for pet '{pet_name}'")

      print(f"{hello_message}, {pet_name}!")  # Print greeting

if __name__ == "__main__":
  try:
      say_hello_to_pets(animals)
  except ValueError as e:
      print(e)