def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
