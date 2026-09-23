import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    result = ""

    for c in string:
        if c == "z":
            result += "z"

    if result == "":
        print("none")
    else:
        print(result)
