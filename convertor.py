def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def main():
    print("Welcome to the Unit Converter!")

    try:
        value = float(input("Enter the value to convert: "))
        print("Select the source unit:")
        print("1. Celsius\n2. Fahrenheit\n3. Meters\n4. Feet\n5. Kilograms\n6. Pounds")

        source_unit = int(input("Enter the number corresponding to the source unit: "))

        print("Select the target unit:")
        target_unit = int(input("Enter the number corresponding to the target unit: "))

        if source_unit == target_unit:
            print("Source and target units are the same. No conversion needed.")
        else:
            result = None
            if source_unit == 1 and target_unit == 2:
                result = celsius_to_fahrenheit(value)
            elif source_unit == 2 and target_unit == 1:
                result = fahrenheit_to_celsius(value)
            elif source_unit == 3 and target_unit == 4:
                result = meters_to_feet(value)
            elif source_unit == 4 and target_unit == 3:
                result = feet_to_meters(value)
            elif source_unit == 5 and target_unit == 6:
                result = kilograms_to_pounds(value)
            elif source_unit == 6 and target_unit == 5:
                result = pounds_to_kilograms(value)
            else:
                print("Conversion not supported. Please select valid source and target units.")
                return

            print(f"The converted value is: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
