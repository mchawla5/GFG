'''
PERFORM INORDER TRAVERSAL WITHOUT RECURSION

The problem requires us to perform inorder traversal without recursion

SOLUTION:
Method: (using stack)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(n)
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
def inorderWithStack(root):
    current  = root
    stack = []

    while(True):
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break


if __name__=='__main__':
    elements = askInput()
    root = createTree(elements)
    inorderWithStack(root)