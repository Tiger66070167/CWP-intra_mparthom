try:
    command = input("What you gotta say? :")
    stopCommand = "STOP"

    while command != stopCommand:
        command = input("I got that! Anything else? :")


except ValueError:
    print("Invalid input. Please enter a valid command.")
    