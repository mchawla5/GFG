'''
CREATE A CIRCULAR LINKED LIST AND PERFORM VARIOUS OPERATIONS

The problem requires us to create a circular list holding data and perform operations like insertion, deletion and search.

SOLUTION:
- Create a class for node
- Create a class for linked list
- Insertion:
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
- Deletion:
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
- Search:
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
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
        self.tail = None
    
    # insert node at beginning
    def insertAtHead(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.tail.next
        self.tail.next = new_node
    
    # insert a node in between
    def insertBetween(self, pos, new_data):
        new_node = Node(new_data)
        head = self.tail.next
        index = 1
        while(index != pos):
            head = head.next
            index +=1
        new_node.next = head.next
        head.next = new_node
        
    # insert a node at the end
    def insertAtTail(self, new_data):
        new_node = Node(new_data)
        if(self.tail is None):
            new_node.next = None
            self.tail = new_node
        elif(self.tail.next is None):
            new_node.next = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    
    # print the list
    def printList(self):
        head = self.tail.next
        if(self.tail is None):
            print("Empty list\n")
        if(head is None):
            print(self.tail.data, end=" ")
        else:
            while(head):
                print(head.data, end=" ")
                head = head.next
                if(head == self.tail.next):
                    break
        print("\n")
    
    # get length of list
    def getLength(self):
        if(self.tail is None):
            return 0
        if(self.tail.next is None):
            return 1
        head = self.tail.next
        count = 0
        while(head):
            count +=1
            head = head.next
            if(head == self.tail.next):
                return count


# Input method (asking user for inputs):
def askInput():
    number = int(input("Enter the number of elements you want to have\n"))
    while(number<1):
        number = int(input("Please enter a valid number\n"))
    linked_list = LinkedList()
    for n in range(0, number):
        linked_list.insertAtTail(int(input("Enter the data value\n")))    
    return linked_list

if __name__=='__main__':
    linked_list = askInput()
    linked_list.printList()
    if(linked_list.getLength() > 0):
        option = int(input("Select one of the options: 1. Insert    2. Delete   3. Search\n"))
        if(option == 1):
            position = int(input("Select the position where you want to insert:     1. Beginning    2. Between  3. End\n"))
            data = int(input("Enter the data you want to insert\n"))
            if(position == 1):
                linked_list.insertAtHead(data)
            elif(position == 2):
                pos = int(input("Enter the place where you want to insert\n"))
                linked_list.insertBetween(pos, data)
            elif(position == 3):
                linked_list.insertAtTail(data)
            else:
                print("no position selected to insert\n")
            linked_list.printList()
        '''elif(option == 2):
            data = int(input("Enter the data you want to delete\n"))
            linked_list.delete(data)
            linked_list.printList()
        elif(option == 3):
            data = int(input("Enter the data you want to search\n"))
            index = linked_list.search(data)
            if(index!=-1):
                print("Found at index "+str(index)+"\n")
            else:
                print("Not found\n")
        else:
            print("No option selected\n")'''
    else:
        print("Linked List not created")