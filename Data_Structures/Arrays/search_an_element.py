'''
SEARCH AN ELEMENT IN A SORTED AND ROTATED ARRAY

The problem requires us to have a function to search an element in a sorted but rotated array.
Eg: arr = [6,7,8,9,1,2,3], element = 1; output: found at index 4

ASSUMPTION: All the elements in array ar distinct

SOLUTION:
- Method 1 (Finding a pivot and then using binary search)
    |_ Time Complexity = O(log n)
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


# Method (Finding a pivot and then using binary search)
def search(arr, l, h, key):
    if (l > h):
        return -1
    mid = (l+h) // 2
    if (arr[mid] == key):
        return mid
    
    if (arr[l] <= arr[mid]):
        if ((key >= arr[l]) and (key <= arr[mid])):
            return search(arr, l, mid-1, key)
        else:
            return search(arr, mid+1, h, key)
    else:
        if ((key >= arr[mid]) and (key <= arr[h])):
            return search(arr, mid+1, h, key)
        return search(arr, l, mid-1, key)


# Main code
if __name__ == "__main__":
    arr, elements_to_rotate = askInput()
    rotateArray(arr, elements_to_rotate)
    key = int(input("Enter the element to find: "))
    found = search(arr, 0, len(arr)-1, key)
    if (found != -1):
        print("Element found at index: ", found)
    else:
        print("Element not found")