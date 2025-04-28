import random

num_side = 6
def main():
 def roll_dice():
    die1 = random.randint(1, num_side)
    die2 = random.randint(1, num_side)
    total = die1 + die2

    print(f"Dice have {num_side} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    main()