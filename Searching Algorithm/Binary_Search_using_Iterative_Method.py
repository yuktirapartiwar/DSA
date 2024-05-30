# WAP to implement Binary Search Algorithm using Iterative Method

# Function to implement Iterative Binary Search
def iterativeBinarySearch(arr, low, high, x):

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return - 1

# Driver Code
if __name__ == '__main__':
    arr = [2, 4, 6, 25, 47]
    x = 25

    # Function call
    result = iterativeBinarySearch(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element found at index ", result)
    else:
        print("Element not found")