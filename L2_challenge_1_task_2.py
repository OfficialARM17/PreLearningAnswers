def number_to_reversed_array(n):

    return [int(digit) for digit in str(n)][::-1]

def main():

    user_input = input("Enter a non-negative number: ")

    # Validate the input to ensure it's a valid non-negative integer
    if user_input.isdigit():
        number = int(user_input)
        result = number_to_reversed_array(number)
        print(f"Reversed digits: {result}")
    else:
        print("Invalid input! Please enter a non-negative integer.")

main()
