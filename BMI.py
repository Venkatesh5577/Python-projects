def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI)
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    """
    Return BMI category based on value
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI CALCULATOR ===")

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (meters): "))

        if weight <= 0 or height <= 0:
            raise ValueError("Height and weight must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
