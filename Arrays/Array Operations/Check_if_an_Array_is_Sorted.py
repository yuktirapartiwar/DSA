# Given an array of size n, WAP to check if it is sorted in ascending order or not.

# Function Definition
def arraySortedOrNot(arr, N):
    if(N==0 or N==1):
        return True
    for i in range(N-2):
        if arr[i] > arr[i+1]:
            return False
    
    return True

# Driver code
arr = [20, 23, 23, 45, 78, 88]
N = len(arr)

if(arraySortedOrNot(arr, N)):
    print("Yes")
else:
    print("No")