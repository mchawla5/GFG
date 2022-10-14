'''
GET ALL POSSIBLE BINARY TREES FROM GIVEN INORDER TRAVERSAL AND PRINT POSTORDER TRAVERSAL

The problem requires us to get all the possible binary tree forms from a given inorder traversal. Eg:
Input:   in[] = {4, 5, 7};
Output:  Preorder traversals of different possible Binary Trees are:
          4 5 7 
          4 7 5 
          5 4 7 
          7 4 5 
          7 5 4 
Below are different possible binary trees
  4         4           5         7       7
   \          \       /   \      /       /
    5          7     4     7    4       5
     \        /                  \     /
      7      5                    5   4 

SOLUTION:
    |_ Time Complexity = O(n3)
    |_ Space Complexity = O(1)
'''

# node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# preorder traversal
def preorder(temp):
    if (temp is None):
        return
    print(temp.data, end=" ")
    preorder(temp.left)
    preorder(temp.right)

def getTrees(inorder_arr, start, end):
    trees = []
    if start > end:
        trees.append(None)
        return trees
    for i in range(start, end+1):
        left_trees = getTrees(inorder_arr, start, i-1)
        right_trees = getTrees(inorder_arr, i+1, end)
        for j in left_trees:
            for k in right_trees:
                node = Node(inorder_arr[i])
                node.left = j
                node.right = k
                trees.append(node)
    return trees


if __name__=='__main__':
    inorder_array = [4, 5, 7]
    n = len(inorder_array)
    trees = getTrees(inorder_array, 0 , n-1)
    print("Preorder traversals: ")
    for i in trees:
        preorder(i)
        print("")