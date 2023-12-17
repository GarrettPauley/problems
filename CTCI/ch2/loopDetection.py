"""
Given the head of a linked list which might contain a loop, return the the node at the beginning of the 
loop else return None

i.e., list = A -> B -> C -> D -> E -> C (same reference to the last C)
output = C
"""
from LinkedList import ListNode


def solution(head):
    slow = head
    fast = head 

    while fast and fast.next: 
        slow = slow.next 
        fast = fast.next.next
        if slow == fast: 
            return slow

    return None

A = ListNode(1, None)
B = ListNode(2, None)
C = ListNode(3, None)

A.next = B
B.next = C
C.next = A #Loop

print(solution(A))