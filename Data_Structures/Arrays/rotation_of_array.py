'''
ROTATION OF ARRAY

The problem requires us to have function to rotate an array 'arr' of size 'n' by a number of elements 'd'

Eg: arr = [1,2,3,4,5,6] if rotated by d=3, output = [4,5,6,1,2,3]
'''

# Input method (asking user for inputs):
def _ask_input():
    size = int(input("Enter the size of array: "))
    
    arr = []
    
    for i in range(size):
        arr.append(int(input("Enter the value into array: ")))
        
    print("arr[{}] = {}".format(size, arr))
    
    elements_to_rotate = int(input("Enter the elements you want to rotate: "))
    return arr, elements_to_rotate


# Method 1 (using a temp array):
def rotate_array_m1(arr, elements_to_rotate):
    new_arr = []
    new_arr = arr[elements_to_rotate:] + arr[0:elements_to_rotate]
    print(new_arr)


if __name__ == "__main__":
    arr, elements_to_rotate = _ask_input()
    rotate_array_m1(arr, elements_to_rotate)