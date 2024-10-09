# Creating the initial dictionary with the four examples
people = [
    {"First name": "Jane", "Last name": "Doe", "Age": 42, "Employed": "Yes"},
    {"First name": "Tom", "Last name": "Smith", "Age": 18, "Employed": "Yes"},
    {"First name": "Mariam", "Last name": "Coulter", "Age": 66, "Employed": "No"},
    {"First name": "Gregory", "Last name": "Tims", "Age": 8, "Employed": "No"}
]
# Function to correctly format the list of people
def display_people(people_list):

    for person in people_list:
        full_name = f"{person['First name']} {person['Last name']}"
        print(f"Name: {full_name}")
        print(f"Age: {person['Age']}")
        print(f"Employed: {person['Employed']}")
        print("-" * 30)
# Function to add a person to the dictionary
def add_person():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    # Validate age is a number
    while not age.isdigit():
        age = input("Please enter a valid age (number): ")
    employed = input("Are they employed? (Yes/No): ").capitalize()
    # Ensure employment status is either 'Yes' or 'No'
    while employed not in ["Yes", "No"]:
        employed = input("Please enter 'Yes' or 'No' for employment: ").capitalize()
    # Saving the details inputted to each section of the dictionary
    new_person = {
        "First name": first_name,
        "Last name": last_name,
        "Age": int(age),
        "Employed": employed
    }
    people.append(new_person)
    print(f"\n{first_name} {last_name} has been added!\n")
# Function to remove a person from the dictionary
def remove_person():
    name_to_remove = input("Enter the first name of the person to remove: ")

    # Find the person with the given first name
    person_found = False
    for person in people:
        if person["First name"].lower() == name_to_remove.lower():
            people.remove(person)
            print(f"\n{name_to_remove} has been removed!\n")
            person_found = True
            break

    if not person_found:
        print(f"\nNo person found with the name {name_to_remove}.\n")

def main():
    while True:
        # Step 2: Display all people
        print("\nCurrent list of people:")
        display_people(people)

        # Step 3: Ask the user for an action
        action = input("What would you like to do? (Add/Remove): ").capitalize()

        if action == "Add":
            add_person() 
        elif action == "Remove":
            remove_person()
        else:
            print("Invalid action. Please type 'Add' or 'Remove'.")
        continue_prompt = input("Would you like to perform another action? (Yes/No): ").capitalize()
        if continue_prompt != "Yes":
            print("Goodbye!")
            break
main()
