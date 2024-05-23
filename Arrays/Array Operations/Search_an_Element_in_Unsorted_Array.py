# WAP to search an element in unsorted array

def search(arr, element, N):
    for i in range(N):
        if (arr[i] == element):
            return i
    return -1


# Driver's code
if __name__ == "__main__":
    arr = [1, 423, 45, 65, 23, 3, 90, 56, 34, 9]
    element = 23
    N = len(arr)

    # Search Operation
    index = search(arr, element, N)
    if index != -1:
        print("Element Found at Position: ", (index + 1))
    else:
        print("Element Not Found")