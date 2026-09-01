"""
BMI Calculator
A simple command-line tool to calculate and classify Body Mass Index (BMI).
"""


def get_positive_float(prompt: str) -> float:
    """
    Prompt the user for a positive number.
    Keeps asking until valid input is given.
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 65.5).\n")
            continue

        if value <= 0:
            print("Value must be greater than zero. Please try again.\n")
            continue

        return value


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters."""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def classify_bmi(bmi: float) -> str:
    """Return the BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obesity"


def main():
    print("=== BMI Calculator ===\n")

    weight_kg = get_positive_float("Enter your weight in kilograms: ")
    height_m = get_positive_float("Enter your height in meters: ")

    bmi = calculate_bmi(weight_kg, height_m)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
