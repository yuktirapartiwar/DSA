# WAP to traverse a given Matrix Using Recursion

# Define the dimensions of the matrix
N = 3
M = 3

# Function to traverse the matrix
def traverse(arr, i, j):
    
    # Check if the current position is the bottom right corner
    # of the matrix. If yes, print the value at that position
    # and end the recursion
    if i == N-1 and j == M-1:
        print(arr[i][j])
        return
    
    # Print the value at the current position
    print(arr[i][j], end=", ")

    # Row Traversal
    if j < M-1:
        traverse(arr, i, j+1)

    # Column Traversal
    elif i < N-1:
        traverse(arr, i+1, 0)


# Driver Code
if __name__ == '__main__':

    # Define the matrix
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Function call to traverse the matrix from top-left corner
    traverse(arr, 0, 0)