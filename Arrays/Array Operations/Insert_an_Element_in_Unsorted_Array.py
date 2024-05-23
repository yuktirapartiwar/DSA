# WAP to insert an element in unsorted array

# Insert Function
def insert(arr, element):
    return arr.append(element)

# Driver's code
if __name__ == '__main__':
    arr = [1, 423, 45, 65, 23, 3, 90, 56, 34, 9]
    element = 40

    # Function Call
    insert(arr, element)

    # Print Output
    print(arr)