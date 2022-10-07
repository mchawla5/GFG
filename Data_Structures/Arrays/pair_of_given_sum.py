'''
FIND A PAIR OF GIVEN SUM IN A SORTED AND ROTATED ARRAY

The problem requires us to find a pair of elements in a sorted but rotated array.
Eg: arr = [6,7,8,9,1,2,3], sum = 5; output: (2,3)

SOLUTION:
- Method 1 (Finding the pivot with O(n))
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
- Method 2 (Finding the pivot with O(logn))
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
'''
from sys import argv

# Input method (asking user for inputs):
def askInput():
    size = int(input("Enter the size of array: "))
    arr = []
    for i in range(size):
        arr.append(int(input("Enter the values into array in increasing order: ")))
    print("\narr[] = {}".format(arr))
    elements_to_rotate = int(input("\nEnter the number of elements you want to rotate: "))
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

# Method 1 (Finding the pivot with O(n)):
def findPairM1(arr, sum):
    n = len(arr)

    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            break
    
    l = (i+1)%n
    r = i
    count = 0
    l1 = []
    pair = []

    while (l != r):
        if (arr[l] + arr[r] == sum):
            count += 1
            pair.append([arr[r], arr[l]])
            #return arr[r], arr[l]
            if (l == (r -1 + n) % n):
                return pair
            l = (l + 1) % n
            r = (r - 1 + n) % n
        
        elif (arr[l] + arr[r] < sum):
            l = (l + 1)%n
        
        else:
            r = (n + r - 1)%n
    return pair

# Method 2 (Finding the pivot with O(logn)):
def findPairM2(arr, sum):
    print("TBD!")

# Main code
if __name__ == "__main__":
    if (len(argv) > 1):
        arr, elements_to_rotate = askInput()
        rotateArray(arr, elements_to_rotate)
        sum = int(input("Enter the sum to find: "))
        n = len(arr)
        
        if (argv[1] == ('m1' or 'M1')):
            pairs = findPairM1(arr, sum)
        elif (argv[1] == ('m2' or 'M2')):
            findPairM2(arr, sum)
        else:
            print("ERROR: Use one method between 'm1/M1' or 'm2/M2' to run the code")
        
        count = len(pairs)
        if (count == 0):
                print("No pair exists")
        else:
            print("\nArray has elements which create a sum %i: "%(sum))
            print (pairs)
    else:
        print("\nERROR: Please select an argument between 'm1/M1' or 'm2/M2' to run the code with the correspodning method!\n")