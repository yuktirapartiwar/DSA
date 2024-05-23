# Given an array of integers arr[] of size N and an integer, WAP to rotate the array elements
# to the left by d positions

# Rotate Function definition
def rotate(L, d, n):
    d=d%n
    temp = []
    k = L.index(d)
    temp = L[k:] + L[0:k]
    return temp


if __name__ == '__main__':
    arr = [1, 4, 6, 3, 7, 8, 3, 5, 8]
    d = 3
    N = len(arr)

    # Function Call
    arr = rotate(arr, d, N)

    # Print Output
    for i in arr:
        print(i, end=" ")