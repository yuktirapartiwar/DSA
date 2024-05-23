# Given an array, WAP to generate all the possible subarrays of the given array using recursion.

# Function Definition
def printSubarrays(arr, start, end):
    if end == len(arr):
        return
    elif start > end:
        return printSubarrays(arr, 0, end + 1)
    else:
        print(arr[start:end+1])
        return printSubarrays(arr, start+1, end)

# Driver Code
arr = [1, 2, 3]
printSubarrays(arr, 0, 0)