'''
PERFORM POSTORDER TRAVERSAL WHEN YOU HAVE PRE AND INORDER

The problem requires us to perform postorder traversal with given preorder and inorder traversals

SOLUTION:
Method 1: (Array)
    |_ Time Complexity = O(n^2)
    |_ Space Complexity = O(1)
Method 2: (Hashmap)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
'''

def search(arr, key, n):
    for index in range(n):
        if(arr[index] == key):
            return index
    return -1

def postOrder(inorder_arr, preorder_arr, n):
    root_index = search(inorder_arr, preorder_arr[0], n)

    if(root_index != 0):
        postOrder(inorder_arr, preorder_arr[1:n], root_index)
    if(root_index != n-1):
        postOrder(inorder_arr[root_index+1:n], preorder_arr[root_index+1:n], n-root_index-1)
    print(preorder_arr[0], end=" ")

if __name__=='__main__':
    inorder_array = [4,2,5,1,3,6]
    preorder_array = [1,2,4,5,3,6]
    n = len(inorder_array)
    print("Postorder traversal: ")
    postOrder(inorder_array, preorder_array, n)
