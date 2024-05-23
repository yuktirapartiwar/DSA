# WAP to find the last duplicate element in a sorted array.

import sys

# Define an array
arr = [1, 2, 2, 5, 5, 6, 8, 9, 9, 11]

n= len(arr)

# Compare elements to find the last duplicate
for i in range(1, n-1):
    if(arr[i] == arr[i-1]):
        index = i
        element = arr[i]

# Print the results    
if(element):
    print(f"Last Index: {index}\n Last duplicate item: {element}")
else:
    print("No duplicate found")
