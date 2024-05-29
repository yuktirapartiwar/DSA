# WAP a program to rotate matrix clockwise.
# Example - For 4 * 4 matrix
# Input - [1, 2, 3, 4]
#         [5, 6, 7, 8]
#         [9, 10, 11, 12]
#         [13, 14, 15, 16]
# Output - [5, 1, 2, 3]
#          [9, 10, 6, 4]
#          [13, 11, 7, 8]
#          [14, 15, 16, 12]


# Function to rotate a matrix
def rotateMatrix(matrix):
    if not len(matrix):
        return
    
    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while left < right and top < bottom:
        prev = matrix[top+1][left]

        for i in range(left, right+1):
            current = matrix[top][i]
            matrix[top][i] = prev
            prev = current

        top += 1

        for i in range(top, bottom+1):
            current = matrix[i][right]
            matrix[i][right] = prev
            prev = current

        right -= 1

        for i in range(right, left-1, -1):
            current = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = current

        bottom -= 1

        for i in range(bottom, top-1, -1):
            current = matrix[i][left]
            matrix[i][left] = prev
            prev = current

        left += 1

    return matrix

# Function to print a matrix
def printMatrix(matrix):
    for row in matrix:
        print(row)

# Driver Code
if __name__ == '__main__':

    # Define a matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    # Print Input Matrix
    print("Input Matrix: ")
    printMatrix(matrix)

    # Print Modified Matrix
    print("\n\nOutput Matrix: ")
    # Function call to rotate the matrix
    rotateMatrix(matrix)
    printMatrix(matrix)