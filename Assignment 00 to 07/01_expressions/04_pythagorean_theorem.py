import math
def main():
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
    bc = math.sqrt(ab**2 + ac**2)
    print(f"The length of hypotenuse is {bc}")
if __name__ == '__main__':
    main()