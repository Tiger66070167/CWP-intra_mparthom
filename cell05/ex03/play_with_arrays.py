array = [2, 8, 9, 48, 8, 22,-12, 2]

new_array = []
i = 0
while i < len(array):
    j = array[i] + 2

    if j > 5 and j not in new_array:
        new_array.append(j)
    i += 1

print("Original array:", array)
print("New array:", new_array)
