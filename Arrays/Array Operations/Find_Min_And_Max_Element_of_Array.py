# WAP to find minimum and maximum element of a given array

import sys

# Define an array
a = [1, 423, 45, 65, 23, 3, 90, 56, 34, 9]

# Sort the array using Built-in sorted() function
a_sorted = sorted(a)

# Find the min and max value
min_value = a_sorted[0]
max_value = a_sorted[-1]

# Print the results
print(f"min: {min_value} max: {max_value}")