"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""
import unittest

class Node: 
    def __init__(self, val, next = None): 
        self.val= val
        self.next = next

    def __str__(self) -> str:
        node_vals = []
        n = self
        while n: 
            node_vals.append(str(n.val))
            n = n.next
        return ' -> '.join(node_vals)


class MyLinkedList:
    def __init__(self, head = None): 
        self.head = head

    def get(self, index: int) -> int:
        if self == None or self.head == None: 
            return -1
        i = 0
        temp = self.head
        while temp: 
            if i == index: 
                return temp.val
            temp = temp.next
            i += 1
        return -1
        
    def addAtHead(self, val: int) -> None:
        if self.head == None or self.head.val == None: 
            self.head = Node(val)
            return
        new = Node(val)
        new.next = self.head
        self.head = new
        
         
    def addAtTail(self, val: int) -> None:
        if self.head == None or self.head.val == None: 
            self.head =  Node(val)
            return
        node = Node(val)
        temp = self.head
        while temp.next: 
            temp = temp.next
        temp.next = node


        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0: 
            self.addAtHead(val)
            return
        count = 0
        new_node = Node(val)
        temp = self.head
        while temp: 
            if count == index - 1: 
                new_node.next = temp.next
                temp.next = new_node
            temp = temp.next
            count += 1

        
    def deleteAtIndex(self, index: int) -> None:
        count = 0
        if index == 0: 
            self.head = self.head.next

        temp = self.head
        while temp and temp.next: 
            if count == index - 1: 
                temp.next = temp.next.next
            temp = temp.next
            count += 1


    def __str__(self) -> str:
        node_vals = []
        count = 0
        n = self.head
        while n: 
            node_vals.append(str(n.val) + f"({count})")
            n = n.next
            count += 1
        return ' -> '.join(node_vals)



class TestLinkedList(unittest.TestCase): 
    testNodes = Node(1, Node(2, Node(3, Node(4))))
    testListNull = MyLinkedList(None)



    # GET TESTS
    def testGet(self): 
        testList = MyLinkedList(self.testNodes)  
        expected = 3
        actual = testList.get(2)
        self.assertEqual(actual, expected)
    def testGetInvalidIndex(self): 
        testList = MyLinkedList(self.testNodes)  
        expected = -1
        actual = testList.get(-2)
        self.assertEqual(actual, expected)
    def testGetInvalidIndex2(self): 
        testList = MyLinkedList(self.testNodes)  
        expected = -1
        actual = testList.get(5)
        self.assertEqual(actual, expected)
    def testGetWithOneNode(self): 
        testList = MyLinkedList(Node(1))  
        expected = 1
        actual = testList.get(0)
        self.assertEqual(actual, expected)
    def testGetEmptyList(self): 
        testListNull = MyLinkedList(None)  
        expected = -1
        actual = testListNull.get(0)
        self.assertEqual(actual, expected)
    
    # ADD TO HEAD TESTS
    def testAddtoHead(self): 
        testList = MyLinkedList(self.testNodes)  
        expected = 5
        testList.addAtHead(5)
        actual = testList.head.val # value of head node
        self.assertEqual(actual, expected)
    def testAddtoHead2(self): 

        testListNull = MyLinkedList(None)  
        expected = 5
        testListNull.addAtHead(5)
        actual = testListNull.head.val # value of head node
        self.assertEqual(actual, expected)

    # ADD TO TAIL TESTS
    def testAddtoTail(self): 
        testList = MyLinkedList(self.testNodes)  
        expected = 5
        testList.addAtTail(5)
        actual = testList.get(4) # value of head node
        self.assertEqual(actual, expected)
    def testAddtoTail2(self): 
        testListNull = MyLinkedList(None)
        expected = 5
        testListNull.addAtTail(5)
        actual = testListNull.get(0) # value of head node
        self.assertEqual(actual, expected)
    
    # TEST INSERT AT INDEX
    def testAddAtIndex(self): 
        testList = MyLinkedList(Node(1, Node(2, Node(3, Node(4)))))  
        expected = 1
        testList.addAtIndex(1, 1)
        actual = testList.get(1) # value of head node
        self.assertEqual(actual, expected)
    # TEST DELETE AT INDEX
    def testDeleteAtIndex(self): 
        testList = MyLinkedList(Node(1, Node(2, Node(3, Node(4)))))  
        expected = 3
        testList.deleteAtIndex(1)
        actual = testList.get(1) # value of head node
        self.assertEqual(actual, expected)
    # LeetCode Tests
    def testCase1(self): 
        testList = MyLinkedList(None)  
        testList.addAtHead(1)
        print(testList)
        testList.addAtTail(3)
        print(testList)
        testList.addAtIndex(1, 2)
        print(testList)
        result1 = testList.get(1)
        self.assertEqual(result1, 2)
        testList.deleteAtIndex(1)
        result2 = testList.get(1)
        self.assertEqual(result2, 3)
    
    def testCase2(self): 
        testList = MyLinkedList(None)
        testList.addAtIndex(0, 10)
        testList.addAtIndex(0, 20)
        testList.addAtIndex(1, 30)
        result = testList.get(0)
        self.assertEqual(result, 20)

    def testCase3(self): 
        testList = MyLinkedList(None)
        testList.addAtHead(7)
        testList.addAtHead(2)
        testList.addAtHead(1)
        testList.addAtIndex(3, 0)
        testList.deleteAtIndex(2)
        testList.addAtHead(6)
        testList.addAtTail(4)
        result = testList.get(4)
        self.assertEqual(result,4)
        testList.addAtHead(4)
        testList.addAtIndex(5,0)
        testList.addAtHead(6)

    def testCase4(self): 
        testList = MyLinkedList(None)
        testList.addAtTail(1)
        testList.addAtTail(3)
        print(testList)
        result = testList.get(1)
        self.assertEqual(result, 3)




 

# testList = MyLinkedList(1, MyLinkedList(2, MyLinkedList(3, MyLinkedList(4))))
# print(testList.addAtTail(5))

if __name__ == "__main__": 
    unittest.main()

