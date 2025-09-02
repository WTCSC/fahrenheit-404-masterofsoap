def main():
    print("Welcome to the Temperature Converter!")
    print("-------------------------------------")

    while True:  # Loop for multiple conversions
        print("\nWhat would you like to do?")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Convert Kelvin to Fahrenheit")
        print("4. Convert Fahrenheit to Kelvin")
        print("5. Convert Kelvin to Celsius")
        print("6. Convert Celsius to Kelvin")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            celsius = get_float("Input Celsius Temperature: ")
            fahrenheit = (celsius * 1.8) + 32
            print(f"\n{celsius}°C is {fahrenheit:.2f}°F.")

        elif choice == "2":
            fahrenheit = get_float("Input Fahrenheit Temperature: ")
            celsius = (fahrenheit - 32) / 1.8
            print(f"\n{fahrenheit}°F is {celsius:.2f}°C.")

        elif choice == "3":
            kelvin = get_float("Input Kelvin Temperature: ")
            fahrenheit = 1.8 * (kelvin - 273.15) + 32
            print(f"\n{kelvin}K is {fahrenheit:.2f}°F.")

        elif choice == "4":
            fahrenheit = get_float("Input Fahrenheit Temperature: ")
            kelvin = (fahrenheit - 32) / 1.8 + 273.15
            print(f"\n{fahrenheit}°F is {kelvin:.2f}K.")

        elif choice == "5":
            kelvin = get_float("Input Kelvin Temperature: ")
            celsius = kelvin - 273.15
            print(f"\n{kelvin}K is {celsius:.2f}°C.")

        elif choice == "6":
            celsius = get_float("Input Celsius Temperature: ")
            kelvin = celsius + 273.15
            print(f"\n{celsius}°C is {kelvin:.2f}K.")

        elif choice == "7":
            print("\nThank you for using the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


def get_float(prompt):
    """Helper function to ensure valid float input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")


main()
