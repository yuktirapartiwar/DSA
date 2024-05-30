# WAP to implement Binary Search Algorithm using Recursive Method

# Function to implement Recursive Binary Search
def recursiveBinarySearch(arr, low, high, x):

    if low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            return recursiveBinarySearch(arr, mid + 1, high, x)

        else:
            return recursiveBinarySearch(arr, low, mid - 1, x)

    else:
        return - 1

# Driver Code
if __name__ == '__main__':
    arr = [2, 4, 6, 25, 47]
    x = 25

    # Function call
    result = recursiveBinarySearch(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element found at index ", result)
    else:
        print("Element not found")