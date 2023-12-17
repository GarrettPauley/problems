"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head: ListNode) -> bool: 
    # Add the nodes to a list, if we encounter a node that we have already added to the list then there is a cycle. 
    visited = []
    temp = head
    while temp: 
        if temp in visited: 
            return True
        visited.append(temp)
        temp = temp.next
    return False

def solution2(head: ListNode) -> bool: 
        # Slow / Fast method. 
        # If there is a loop, then the fast pointer will eventuall "catch up" to the slow pointer
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


A = ListNode(1, None)
B = ListNode(2, None)
C = ListNode(3, None)

A.next = B
B.next = C
C.next = A #Loop

print(solution2(A))
    