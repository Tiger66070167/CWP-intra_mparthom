try:

    num = int(input("Enter a number less than 25: "))

    if num > 25:
        print("Error.\n")

    else:
        i = num
        for i in range(num, 26):
            print("Inside the loop, my variable is:", i)


except ValueError:
    print("Invalid input. Please enter an integer value only.")
