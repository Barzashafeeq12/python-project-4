def main():
    print("Welcome to the Planetary Weight Calculator!")
    
    # Prompt user for their Earth weight
    earth_weight = float(input("Enter your weight on Earth: "))
    
    # Prompt user for the planet name
    planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

    # Define gravity constants for each planet (compared to Earth)
    gravity_constants = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Find the gravity constant for the selected planet
    if planet in gravity_constants:
        planet_weight = earth_weight * gravity_constants[planet]
        rounded_weight = round(planet_weight, 2)
        print(f"The equivalent weight on {planet}: {rounded_weight}")
    else:
        print("Invalid planet entered. Please restart and choose a correct planet.")

if __name__ == "__main__":
    main()
