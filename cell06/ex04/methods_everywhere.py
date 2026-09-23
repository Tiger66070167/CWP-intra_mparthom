def shrink(string):
    print(string[0:8])

def enlarge(string):
    
    while len(string) < 8:
        string += "Z"

    print(string)


s = input("Enter a string: ")

if len(s) < 8:
    enlarge(s)

elif len(s) > 8:
    shrink(s)

elif len(s) == 8:
    print(s)

else:
    print("none")