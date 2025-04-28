#07
def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

#08
def print_multiple(message, repeats):
    """
    Prints the message the specified number of times.
    """
    for _ in range(repeats):
        print(message)

def main():
    # Prompt user for input
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the function
    print_multiple(message, repeats)

# This line runs the program
if __name__ == '__main__':
    main()
