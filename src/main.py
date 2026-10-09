from utils import add, subtract, multiply


def main():
    print("Name: Mushfiqur Rahman")
    print("Today's Date: 09 October, 2026")

    try:
        print("\nCalculator Results")
        print("Addition:", add(10, 5))
        print("Subtraction:", subtract(10, 5))
        print("Multiplication:", multiply(10, 5))

    except (TypeError, ValueError) as error:
        print("Calculator error:", error)


if __name__ == "__main__":
    main()
