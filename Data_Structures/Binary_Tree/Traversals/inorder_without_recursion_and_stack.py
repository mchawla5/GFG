'''
PERFORM INORDER TRAVERSAL WITHOUT RECURSION AND STACK

The problem requires us to perform inorder traversal without recursion and without stack. This can be done using Morris traversal which is based on threaded binary tree.

SOLUTION:
Method: (using Morris Traversal)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
'''

# node class
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# insert node
def insert(root, key):
    q = []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

#  Input method (asking user for inputs):
def askInput():
    elements = []
    number = int(input("Enter the number of elements you want to have\n"))
    for n in range(0, number):
        elements.append(int(input("Enter the element\n")))
    return elements

# create a binary tree
def createTree(elements):
    root = Node(elements[0])
    for n in range(1, len(elements)):
        insert(root, elements[n])
    return root

# traverse
def inorderMorris(root):
    current = root

    while current is not None:
        if current.left is None:
            print(current.data, end=" ")
            current = current.right
        else:                                                               # move left if possible
            pre =  current.left                                             
            while ((pre.right is not None) and (pre.right is not current)): # move to rightmost
                pre = pre.right
            if pre.right is None:                                           # rightmost will be none or
                pre.right = current
                current = current.left
            else:                                                           # rightmost will be current
                pre.right = None
                print(current.data, end=" ")
                current = current.right


if __name__=='__main__':
    elements = askInput()
    root = createTree(elements)
    inorderMorris(root)