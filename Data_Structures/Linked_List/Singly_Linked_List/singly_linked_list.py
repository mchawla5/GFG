'''
CREATE A SINGLY LINKED LIST AND PERFORM VARIOUS OPERATIONS

The problem requires us to create a singly list holding data and perform operations like insertion, deletion and search.

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
        self.head = None

    # insert node at beginning
    def insertAtHead(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # insert a node in between
    def insertBetween(self, prev_data, new_data):
        temp = self.head
        while(temp):
            if(temp.data == prev_data):
                new_node = Node(new_data)
                new_node.next = temp.next
                temp.next = new_node
                return
            else:
                temp = temp.next
    
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
    
    # delete a node
    def delete(self, key):
        temp = self.head
        if(temp == None):
            print("Nothing to delete\n")
        elif(temp.data == key):
                self.head = temp.next
                temp = None
        else:
            while(temp is not None):
                if(temp.data == key):
                    break
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp = None
    
    # print the list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")
    
    # get the length
    def getLength(self):
        temp = self.head
        n = 0
        while(temp):
            temp = temp.next
            n+=1
        return n
    
    # search element
    def search(self, new_data):
        temp = self.head
        index = 0
        while(temp):
            if (temp.data == new_data):
                return (index)
            temp = temp.next
            index +=1
        return(-1)


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
                prev = int(input("Enter the data after which you want to insert\n"))
                linked_list.insertBetween(prev, data)
            elif(position == 3):
                linked_list.insertAtTail(data)
            else:
                print("no poistion selected to insert\n")
            linked_list.printList()
        elif(option == 2):
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
            print("No option selected\n")
    else:
        print("Linked List not created")