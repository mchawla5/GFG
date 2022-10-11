'''
CREATE A BINARY TREE AND PERFORM VARIOUS OPERATIONS

The problem requires us to create a binary tree holding data and perform operations like insertion, deletion, and traversal.

SOLUTION:
- Create a class for node
- Create a class for binary tree
- Insertion:
    |_ Time Complexity = O(V)   where V is the number of nodes
    |_ Space Complexity = O(B)  where B is the width of the tree (worst case size of queue)
- Deletion:
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(n)  size of queue
- Traversal:
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

# delete the last node
def deleteLast(root, last):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is last:
            temp = None
            return
        if temp.right:
            if temp.right is last:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is last:
                temp.left = None
                return
            else:
                q.append(temp.left)

# delete the element
def delete(root, key):
    if root is None:
        return None
    if ((root.left is None) and (root.right is None)):
        if root.data == key:
            return None
        else:
            return root
    node_to_delete = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            node_to_delete = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if node_to_delete:
        last_node_data = temp.data
        deleteLast(root, temp)
        node_to_delete.data = last_node_data

# inorder traversal
def inorder(temp):
    if (temp is None):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

# preorder traversal
def preorder(temp):
    if (temp is None):
        return
    print(temp.data, end=" ")
    preorder(temp.left)
    preorder(temp.right)

# postorder traversal
def postorder(temp):
    if (temp is None):
        return
    postorder(temp.left)
    postorder(temp.right)
    print(temp.data, end=" ")

# traverse options
def traverse(root):
    traversal = int(input("How do you want to traverse the tree:    1. Inorder   2. Preorder   3. Postorder\n"))
    if traversal == 2:
        print("Preorder traversal: ")
        preorder(root)
    elif traversal == 3:
        print("Postorder traversal: ")
        postorder(root)
    else:
        print("Inorder traversal: ")
        inorder(root)

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


if __name__=='__main__':
    elements = askInput()
    root = createTree(elements)
    traverse(root)
    option = int(input("\nSelect an option to perform: 1. Insert a node   2. Delete a node\n"))
    if option == 1:
        val = int(input("Enter the value to insert\n"))
        insert(root, val)
    elif option == 2:
        val = int(input("Enter the value to delete\n"))
        delete(root, val)
    else:
        print("No option selected\n")
    traverse(root)