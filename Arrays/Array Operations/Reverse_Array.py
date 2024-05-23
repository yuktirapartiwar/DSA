# WAP to print reverse of the given array

import sys

# Define an array
original_array = [1, 423, 45, 65, 23, 3, 90, 56, 34, 9]

# Reverse array
reversed_array = original_array[::-1]

# Print the results
print("Reversed Array: ")
for i in reversed_array:
    print(i, end=" ")