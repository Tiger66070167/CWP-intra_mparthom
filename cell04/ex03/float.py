try:

    s = input("Enter a string: ")

    if s.isdigit():
        print("This number is an integer")

    elif s.count(".") == 1 and s.replace(".", "").isdigit():
        print("This number is a decimal")
        
    else:
        print("This is not a number")


except KeyboardInterrupt:
    print("\nOperation cancelled by user.")

