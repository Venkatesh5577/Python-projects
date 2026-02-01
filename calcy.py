import math


def calculate(operation, values):
    if operation == "add":
        return values[0] + values[1]

    elif operation == "sub":
        return values[0] - values[1]

    elif operation == "mul":
        return values[0] * values[1]

    elif operation == "div":
        if values[1] == 0:
            raise ValueError("Division by zero")
        return values[0] / values[1]

    elif operation == "power":
        return math.pow(values[0], values[1])

    elif operation == "sqrt":
        if values[0] < 0:
            raise ValueError("Negative number")
        return math.sqrt(values[0])

    elif operation == "log":
        if values[0] <= 0:
            raise ValueError("Invalid input for log")
        return math.log10(values[0])

    elif operation == "ln":
        if values[0] <= 0:
            raise ValueError("Invalid input for ln")
        return math.log(values[0])

    elif operation == "sin":
        return math.sin(math.radians(values[0]))

    elif operation == "cos":
        return math.cos(math.radians(values[0]))

    elif operation == "tan":
        return math.tan(math.radians(values[0]))

    elif operation == "fact":
        if values[0] < 0 or not values[0].is_integer():
            raise ValueError("Factorial only for non-negative integers")
        return math.factorial(int(values[0]))

    else:
        raise ValueError("Invalid operation")


def main():
    try:
        operation = input("Enter operation: ").strip().lower()

        if operation in ["add", "sub", "mul", "div", "power"]:
            a = float(input())
            b = float(input())
            result = calculate(operation, [a, b])

        else:
            a = float(input())
            result = calculate(operation, [a])

        print(result)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
