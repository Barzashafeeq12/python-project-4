def main():
 divide: int = int(input("Please enter an integer to be divided: "))
 divisor:int = int(input("Please enter an integer to divide by: "))
 quotient: int = divide // divisor 
 remainder: int = divide % divisor
 print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()