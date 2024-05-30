# WAP to implement Selection Sort

A = [65, 25, 12, 22, 11]

# Print the given array
print("Given Array: ")
for i in range(len(A)):
    print(A[i], end=" ")

for i in range(len(A)):

    # Find minimum element in the remaining array
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j

    A[i], A[min_index] = A[min_index], A[i] 

# Print the sorted array
print("\nSorted Array: ")
for i in range(len(A)):
    print(A[i], end=" ")
