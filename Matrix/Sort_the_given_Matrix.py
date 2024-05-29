# WAP to sort the given matrix

SIZE = 10

# Functon to sort the given matrix
def sortMatrix(matrix, n):
    temp = [0] * (n*n)
    k = 0

    for i in range(0,n):
        for j in range(0,n):
            temp[k] = matrix[i][j]
            k += 1

    temp.sort()

    k =0

    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = temp[k]
            k += 1

# Function to print given matrix
def printMatrix(matrix, n):
    
    for i in range(0, n):
        for j in range(0,n):
            print(matrix[i][j], end=" ")

        print()

# Driver Code
if __name__ == '__main__':
    matrix = [ [ 5, 4, 7 ],
               [ 1, 3, 8 ],
               [ 2, 9, 6 ] ]
    n = 3

    print("Original Matrix: ")
    printMatrix(matrix, n)

    # Function call to sort the given matrix
    print("Sorted Matrix: ")
    sortMatrix(matrix, n)
    printMatrix(matrix, n)