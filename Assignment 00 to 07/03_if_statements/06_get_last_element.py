def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    print(lst[-1])

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    if lst:  # Check if the list is not empty
        get_last_element(lst)
    else:
        print("The list is empty. No last element.")

if __name__ == '__main__':
    main()
