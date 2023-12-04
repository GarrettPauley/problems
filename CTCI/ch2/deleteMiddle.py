""" 

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


"""

from LinkedList import ListNode
def deleteMiddleSmallBrainedSolution(head) -> ListNode: 
    if not head: # Null list
        return None
    if head.next == None:  # only one element
        return None    
    # how many nodes do we have? 
    temp = head
    count = 0
    while temp: 
        count += 1
        temp = temp.next    
    # Target the middle node
    mid = (count // 2)
    prevNode = head
    temp2 = head
    while mid > 0:
        prevNode = temp2
        temp2 = temp2.next
        mid -= 1
    #The node before the middle should point to the node after the middle. Deleting the middle node. 
    prevNode.next = prevNode.next.next
    return head 


def deleteMiddleBigBrain(head) -> ListNode: 
    """ use slow and fast pointers"""
    #Give the fast pointer a head-start. This way the slow pointer will actually 
    # point to the node before the middle

    fast = head.next.next
    slow = head

    if not head or not head.next: #Null head or only one element: 
        return None
    
    # Otherwise, find the middle node and delete it
    while fast and fast.next: 
        fast = fast.next.next
        slow = slow.next
    # Delete the middle
    slow.next = slow.next.next
    return head

t = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
t2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(t)
print(deleteMiddleBigBrain(t))