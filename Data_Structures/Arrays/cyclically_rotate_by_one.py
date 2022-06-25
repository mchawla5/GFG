'''
CYCLICALLY ROTATE ARRAY BY ONE

The problem requires us to have a function to rotate an array 'arr' of size 'n' clockwise by one element

Eg: arr = [1,2,3,4,5,6], output = [6,1,2,3,4,5]

SOLUTION:
- Method 1 (using a temp variable)
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(1)
- Method 2 (using two pointers)
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(1)
- Method 3 (using slicing)
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(1)
'''
from sys import argv


# Input method (asking user for inputs):
def askInput():
    size = int(input("Enter the size of array: "))
    arr = []
    for i in range(size):
        arr.append(int(input("Enter the value into array: ")))
    print("\narr[] = {}".format(arr))
    return arr, size


# Method 1 (using a temp variable)
def rotateArrayM1(arr, n):
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    print(arr)


# Method 2 (using two pointers)
def rotateArrayM2(arr, n):
    i = 0
    j = n-1
    while i != j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    print(arr)
    

# Method 3 (using slicing)
def rotateArrayM3(arr, n):
    arr[:] = arr[-1:]+arr[:-1]
    print(arr)


# Main code
if __name__ == "__main__":
    if (len(argv) > 1):
        arr, n = askInput()
        if (argv[1] == ('m1' or 'M1')):
            rotateArrayM1(arr, n)
        elif (argv[1] == ('m2' or 'M2')):
            rotateArrayM2(arr, n)
        elif (argv[1] == ('m3' or 'M3')):
            rotateArrayM3(arr, n)
    else:
        print("\nERROR: Please select an argument between 'm1/M1' or 'm2/M2' to run the code with the correspodning method!\n")