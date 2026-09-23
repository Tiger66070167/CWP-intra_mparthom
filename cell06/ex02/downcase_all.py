import sys


def downcase_it(string):
    return string.lower()


if len(sys.argv) == 1:
    print("none")
else:
    i = 1
    while i < len(sys.argv):
        print(downcase_it(sys.argv[i]))
        i += 1
