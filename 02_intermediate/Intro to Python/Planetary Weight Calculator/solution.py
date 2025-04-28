def calculate_weight(earth_weight, planet):
    # Define the gravity constants for each planet
    gravity_constants = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Check if the entered planet is valid
    if planet in gravity_constants:
        planet_weight = earth_weight * gravity_constants[planet]
        return round(planet_weight, 2)
    else:
        return None


def main():
    print("Welcome to the Planetary Weight Calculator!")
    
    # Prompt user for their weight on Earth
    earth_weight = float(input("Enter your weight on Earth: "))
    
    # Show a list of planets and ask for a selection
    print("\nSelect a planet to calculate your weight on:")
    print("1. Mercury")
    print("2. Venus")
    print("3. Mars")
    print("4. Jupiter")
    print("5. Saturn")
    print("6. Uranus")
    print("7. Neptune")
    
    # Get user's choice
    choice = input("\nEnter the number corresponding to the planet: ")
    
    # Map choice to planet name
    planet_map = {
        "1": "Mercury",
        "2": "Venus",
        "3": "Mars",
        "4": "Jupiter",
        "5": "Saturn",
        "6": "Uranus",
        "7": "Neptune"
    }

    # Check if the choice is valid
    if choice in planet_map:
        planet = planet_map[choice]
        # Calculate the weight on the selected planet
        planet_weight = calculate_weight(earth_weight, planet)
        if planet_weight is not None:
            print(f"\nThe equivalent weight on {planet}: {planet_weight}")
        else:
            print("Error: Invalid planet name.")
    else:
        print("Error: Invalid selection. Please choose a valid number between 1 and 7.")

if __name__ == "__main__":
    main()
