array = [2, 8, 9, 48, 8, 22,-12, 2]

print("Original array:", array)

print("New array: [", end="")
i = 0
while i < len(array):
    j = array[i]+2
    print("{}".format(j), end="")
    i += 1
    if i < len(array):
        print(", ", end="")

print("]")
