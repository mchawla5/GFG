'''
COUNT THE NUMBER OF TIMES AN ELEMENT IS PRESENT

The problem requires us to create a singly list holding data and perform operations like insertion, deletion and search.

SOLUTION:
- Create a class for node
- Create a class for linked list
- Method 1:
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
- Method 2: (recursion)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(n)
'''

# node class
class Node:
    # initialise object
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    # initialise object
    def __init__(self):
        self.head = None
        self.count = 0
    
    # insert a node at the end
    def insertAtTail(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = new_node
    
    # print the list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")
    
    # count the element using method 1
    def count_m1(self, key):
        curr = self.head
        while(curr):
            if(curr.data == key):
                self.count +=1
            curr = curr.next
        return self.count
    
    # count the element using method 2
    def count_m2(self, node, key):
        if(node is None):
            return self.count
        if(node.data == key):
            self.count +=1
        return self.count_m2(node.next, key)


# Input method (asking user for inputs):
def askInput():
    number = int(input("Enter the number of elements you want to have in the linked list\n"))
    while(number<1):
        number = int(input("Please enter a valid number\n"))
    linked_list = LinkedList()
    for n in range(0, number):
        linked_list.insertAtTail(int(input("Enter the data value\n")))    
    return linked_list


if __name__=='__main__':
    linked_list = askInput()
    linked_list.printList()
    key = int(input("Enter the element you want to count\n"))
    option = int(input("Choose the method you want to use:  1. Method-1     2. Method-2\n"))
    if(option == 1):
        count = linked_list.count_m1(key)
        print("count = "+str(count))
    elif(option == 2):
        count = linked_list.count_m2(linked_list.head, key)
        print("count = "+str(count))
    else:
        print("No option was selected\n")