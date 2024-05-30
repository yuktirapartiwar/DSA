# WAP to implement Linear Search Algorithm

# Function to implement Linear Search
def linearSearch(arr, N, x):
    for i in range(0, N):
        if(arr[i] == x):
            print("Element found at index: ", i)
            return
    print("Element not found.")
    
# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    N = len(arr)
    x = 10

    # Function Call
    linearSearch(arr, N, x)