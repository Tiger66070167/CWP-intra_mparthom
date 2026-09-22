try:
    num = int(input("Enter a number: "))

    i = 0
    while i <= num:
        print(i, "x", num, "=", num * i)
        i += 1


except ValueError:
    print("Invalid input. Please enter an integer value only.")
