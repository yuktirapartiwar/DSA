# WAP to find transpose of a given Matrix

N = 4

# Function to find transpose of matrix A and store it in matrix B
def transpose(A, B):
    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]

# Function to print Matrix
def printMatrix(matrix):
    
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")

        print()

# Driver Code
if __name__ == '__main__':
    A = [[1, 1, 1, 1],
         [2, 2, 2, 2],
         [3, 3, 3, 3],
         [4, 4, 4, 4]]
    
    B = [[0 for i in range(N)] for j in range(N)]

    print("Original Matrix: ")
    printMatrix(A)

    # Function call to transpose matrix A
    transpose(A, B)

    print("Transposed Matrix: ")
    printMatrix(B)