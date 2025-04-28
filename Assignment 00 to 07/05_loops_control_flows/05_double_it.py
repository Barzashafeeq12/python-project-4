def main():
    # Ask the user to enter a number
    curr_value = int(input("Please enter a number: "))

    # Double the number and print it until it's greater than or equal to 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

if __name__ == '__main__':
    main()
