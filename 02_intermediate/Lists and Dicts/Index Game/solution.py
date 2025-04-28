import random

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return "Element updated successfully."
    except IndexError:
        return "Index out of range."

def slice_list(lst, start_index, end_index):
    if start_index < 0 or end_index > len(lst) or start_index > end_index:
        return "Invalid slice indices."
    return lst[start_index:end_index]

def main():
    # --- Problem 1: List Practice ---
    print("Welcome to the List Practice and Index Game!")
    print("---------------------------------------------")
    
    # Create fruit_list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Initial fruit list:", fruit_list)

    # Print the length of the list
    print("Length of fruit_list:", len(fruit_list))

    # Add 'mango' to the end
    fruit_list.append('mango')

    # Print the updated list
    print("Updated fruit_list:", fruit_list)
    
    # Use fruit_list for the Index Game
    my_list = fruit_list

    # --- Problem 2: Index Game ---
    while True:
        print("\nCurrent List:", my_list)
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(result)

        elif choice == '3':
            start_index = int(input("Enter the start index: "))
            end_index = int(input("Enter the end index: "))
            result = slice_list(my_list, start_index, end_index)
            print("Sliced list:", result)

        elif choice == '4':
            print("Thanks for playing the index game!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
