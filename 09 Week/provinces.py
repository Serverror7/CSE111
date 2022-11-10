import json
# Open the provinces.txt file for reading.
provinces = []
f = open('provinces.txt', 'r')
# Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
for x in f:
    provinces.append(f.readline())
provinces = [x[:-1] for x in provinces]
# Print the entire list.
print(provinces)
# Remove the first element from the list.
provinces.pop(0)
# Remove the last element from the list.
last_element_index = len(provinces) - 1
provinces.pop(last_element_index)
# Replace all occurrences of "AB" in the list with "Alberta".
count = 0
for x in provinces:
    if x == 'AB':
        provinces[count] = 'Alberta'
    count = count + 1
print(provinces)
# Count the number of elements that are "Alberta" and print that number.
count = 0
for x in provinces:
    if x == 'Alberta':
        count = count + 1
print(count)