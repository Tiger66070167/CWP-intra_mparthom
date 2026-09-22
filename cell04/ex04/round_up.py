import math

try:
    num = float(input("Enter a number: "))

    print(math.ceil(num))


except ValueError:
    print("Invalid input. Please enter a valid number.")
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
