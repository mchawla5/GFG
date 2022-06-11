'''
ROTATION OF ARRAY

The problem requires us to have function to rotate an array 'arr' of size 'n' by a number of elements 'd'

Eg: arr = [1,2,3,4,5,6] if rotated by d=3, output = [4,5,6,1,2,3]

SOLUTION:
- Method 1
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(n)
- Method 2
    |_ Time Complexity = O(n)
    |_ Auxiliary Space = O(1)
'''
from sys import argv
import time


# Input method (asking user for inputs):
def _ask_input():
    size = int(input("Enter the size of array: "))
    arr = []
    for i in range(size):
        arr.append(int(input("Enter the value into array: ")))
    print("\narr[{}] = {}".format(size, arr))
    elements_to_rotate = int(input("\nEnter the elements you want to rotate: "))
    return arr, elements_to_rotate


# Method 1 (using a temp array):
def _rotate_array_m1(arr, elements_to_rotate):
    new_arr = []
    new_arr = arr[elements_to_rotate:] + arr[0:elements_to_rotate]
    print(new_arr)


# Method 2 (using a GCD value):
def _gcd(a,b):
    if (b == 0):
        return a
    else:
        return _gcd(b, a%b)

def _rotate_array_m2(arr, elements_to_rotate):
    n = len(arr)
    d = elements_to_rotate % n
    gcd = _gcd(d,n)
    for i in range(gcd):
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


# Main code
if __name__ == "__main__":
    if (len(argv) > 1):
        arr, elements_to_rotate = _ask_input()
        if (argv[1] == ('m1' or 'M1')):
            _rotate_array_m1(arr, elements_to_rotate)
        elif (argv[1] == ('m2' or 'M2')):
            _rotate_array_m2(arr, elements_to_rotate)
    else:
        print("Please select an argument between 'm1/M1' or 'm2/M2' to select the method to run the code!")