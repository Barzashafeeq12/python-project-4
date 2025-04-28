import random

num_side = 6

def roll_dice():
    die1 = random.randint(1, num_side)
    die2 = random.randint(1, num_side)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    die1 = 10
    print(f"die1 in main() starts as {die1}")
    for _ in range(3):
        roll_dice()
        print(f"die1 in main() still {die1}")

main()
