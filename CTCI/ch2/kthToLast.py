"""
Given the head of a linked list, return the kth elements from the end the list. 

i.e., list = 1 -> 2 -> 3 -> 4 -> 5 ; k= 2 
output = 2
"""
from LinkedList import ListNode


def solution(head, k): 
    count = 0
    temp = head
    temp2 = head
    while temp: 
        count += 1
        temp = temp.next
    
    count = count - k
    prevNode = None
    while count > 0:
        prevNode = temp2
        temp2 = temp2.next
        count -= 1
    # delete the node
    return deleteNode(head, temp2)

def solution2(head, k): 
    fast = head
    slow = head
    # Give the fast pointer a head start
    for i in range(k): 
        fast = fast.next
    # keep going until the fast pointer reaches the end
    while fast.next: 
        fast = fast.next 
        slow = slow.next 
    # At this point, the slow pointer will be at the k'th node from the end. 
    # We want to delete it.
    slow.next = slow.next.next
    return head


def deleteNode(head, delete): 
    temp = head
    while temp.next != None: 
        if temp.next == delete: 
            temp.next = temp.next.next
            return head
        temp = temp.next
    return head






targetNode = ListNode(7)
t = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,targetNode)))))
print(t)
#print(deleteNode(t, targetNode))
t2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#print(solution(t2, 2))
print(solution2(t2, 2))