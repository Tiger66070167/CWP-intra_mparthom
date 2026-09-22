import string

try:
    s = input("Enter a string: ")

    for char in s:
        if char in string.ascii_lowercase:
            print(char.upper(), end="")
            
        else:
            print(char.lower(), end="")

except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
