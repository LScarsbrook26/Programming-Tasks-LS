"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

while True:
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose an option 1, 2 or 3: ")

    if choice == "1":
        temperature = input("Enter temperature in Celsius: ")
        if temperature == "":
            print("Invalid input.")
        else:
            temperature = float(temperature)
            fahrenheit = (temperature * 9 / 5) + 32
            print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == "2":
        temperature = input("Enter temperature in Fahrenheit: ")

        if temperature == "":
            print("Invalid input.")
        else:
            temperature = float(temperature)
            celsius = (temperature - 32) * 5 / 9
            print("Temperature in Celsius:", celsius)

    elif choice == "3":
        print("exit ")
        break
    else:
        print("Invalid choice. Please choose 1, 2 or 3.")
