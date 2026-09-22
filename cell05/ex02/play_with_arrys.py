array = [2, 8, 9, 48, 8, 22,-12, 2]

print("Original array:", array)

new_array = []
i = 0
while i < len(array):
    j = array[i] + 2

    if j > 5:
        new_array.append(j)
    i += 1

print("New array:", new_array)
