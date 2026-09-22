try:
    age = int(input("Please tell me your age: "))

    print("You are currently {} years old.".format(age))

    for i in range(1, 4):
        print("In {} years, you'll be {} years old.".format(i*10, age + i*10))


except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
