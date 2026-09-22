try:
    first_number = float(input("Give me the first number: "))
    second_number = float(input("Give me the second number: "))

    print("Thank you!")
    print(first_number, "+", second_number, "=", first_number + second_number)
    print(first_number, "-", second_number, "=", first_number - second_number)
    print(first_number, "/", second_number, "=", first_number / second_number)
    print(first_number, "*", second_number, "=", first_number * second_number)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
