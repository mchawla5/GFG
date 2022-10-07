'''
FIND THE MINIMUM ELEMENT IN A SORTED AND ROTATED ARRAY

The problem requires us to find the minimum element in a sorted but rotated array.
Eg: arr = [6,7,8,9,1,2,3]; output: 1 at index 4

SOLUTION:
- Method 1
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
- Method 2 (Using binary search)
    |_ Time Complexity = O(logn)
    |_ Space Complexity = O(1)
'''
from sys import argv

# Input method (asking user for inputs):
def askInput():
    size = int(input("Enter the size of array: "))
    arr = []
    for i in range(size):
        arr.append(int(input("Enter the value into array: ")))
    print("\narr[] = {}".format(arr))
    elements_to_rotate = int(input("\nEnter the elements you want to rotate: "))
    return arr, elements_to_rotate

# Rotating the array:
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotateArray(arr, elements_to_rotate):
    if (elements_to_rotate == 0):
        print(arr)
        return
    n = len(arr)
    d = elements_to_rotate % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    print(arr)
    print("\n")


# Method 1:
def findMinM1(arr, low, high):
    if (high < low):            # if array isn't rotated
        return arr[0]
    if (high == low):           # if array has only one element
        return arr[low]
    
    mid = int((low + high)/2)

    if ((mid < high) and (arr[mid+1] < arr[mid])):      # case where mid+1 is the min element
        return arr[mid+1]
    if ((mid > low) and (arr[mid] < arr[mid-1])):       # if mid is min
        return arr[mid]
    if (arr[high] > arr[mid]):                          # check if need to go left or right
        return findMinM1(arr, low, mid-1)
    else:
        return findMinM1(arr, mid+1, high)


# Method 2:
def findMinM2(arr, low, high):
    while (low < high):
        mid = low + (high - low) // 2

        if (arr[mid] == arr[high]):
            high = -1
        elif (arr[mid] > arr[high]):
            low = mid+1
        else:
            high = mid
    return arr[high]


# Main code
if __name__ == "__main__":
    if (len(argv) > 1):
        arr, elements_to_rotate = askInput()
        rotateArray(arr, elements_to_rotate)
        n = len(arr)

        if (argv[1] == ('m1' or 'M1')):
            min = findMinM1(arr, 0, n-1)
        elif (argv[1] == ('m2' or 'M2')):
            min = findMinM2(arr, 0, n-1)
        print(min)
    else:
        print("\nERROR: Please select an argument between 'm1/M1' or 'm2/M2' to run the code with the correspodning method!\n")