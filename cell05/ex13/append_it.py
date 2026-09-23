import sys

if len(sys.argv) == 1:
    print("none")
else:
    i = 1
    while i < len(sys.argv):
        word = sys.argv[i]

        if not word.endswith("ism"):
            print(word + "ism")

        i += 1
