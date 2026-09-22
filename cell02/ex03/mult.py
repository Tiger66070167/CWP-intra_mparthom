try:

    firstNum = float(input("Enter the first number: "))
    secondNum = float(input("Enter the second number: "))

    sum = firstNum * secondNum

    if sum > 0:
        print(sum, "\nThe result is positive.")
    elif sum < 0:
        print(sum, "\nThe result is negative.")
    else:
        print(sum, "\nThe result is zero.")

except ValueError:
    print("Invalid input. Please enter numeric values only.")
