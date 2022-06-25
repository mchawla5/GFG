'''
ROTATION OF ARRAY

The problem requires us to have a function to rotate an array 'arr' of size 'n' by a number of elements 'd'

Eg: arr = [1,2,3,4,5,6] if rotated by d=3, output = [4,5,6,1,2,3]

SOLUTION:
- Method 1
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(n)
- Method 2
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(1)
- Method 3
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(1)
'''
from sys import argv
import time


# Input method (asking user for inputs):
def askInput():
    size = int(input("Enter the size of array: "))
    arr = []
    for i in range(size):
        arr.append(int(input("Enter the value into array: ")))
    print("\narr[] = {}".format(arr))
    elements_to_rotate = int(input("\nEnter the elements you want to rotate: "))
    return arr, elements_to_rotate


# Method 1 (using a temp array):
def rotateArrayM1(arr, elements_to_rotate):
    new_arr = []
    new_arr = arr[elements_to_rotate:] + arr[0:elements_to_rotate]
    print(new_arr)


# Method 2 (using a GCD value):
def gcd(a,b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

def rotateArrayM2(arr, elements_to_rotate):
    n = len(arr)
    d = elements_to_rotate % n
    gcd_value = gcd(d,n)
    for i in range(gcd_value):
        temp = arr[i]
        j = i
        while 1:
            k = j+d
            if k >= n:
                k = k-n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    print(arr)


# Method 3 (reversal algorithm):
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotateArrayM3(arr, elements_to_rotate):
    if elements_to_rotate == 0:
        return
    n = len(arr)
    d = elements_to_rotate % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    print(arr)


# Main code
if __name__ == "__main__":
    if (len(argv) > 1):
        arr, elements_to_rotate = askInput()
        if (argv[1] == ('m1' or 'M1')):
            rotateArrayM1(arr, elements_to_rotate)
        elif (argv[1] == ('m2' or 'M2')):
            rotateArrayM2(arr, elements_to_rotate)
        elif (argv[1] == ('m3' or 'M3')):
            rotateArrayM3(arr, elements_to_rotate)
    else:
        print("\nERROR: Please select an argument between 'm1/M1' or 'm2/M2' to run the code with the correspodning method!\n")