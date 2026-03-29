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


h = float(input("Enter your height in meters: "))
w = float(input("Enter your Weight in Kg: "))

BMI = w / (h * h)
print("BMI Calculated is:  ", BMI)

if (BMI > 0):
    if (BMI <= 16):
        print("You are very underweight")
    elif (BMI <= 18.5):
        print("You are underweight")
    elif (BMI <= 25):
        print("Congrats! You are Healthy")
    elif (BMI <= 30):
        print("You are overweight")
    else:
        print("You are very overweight")
else:
    print("enter valid details")
