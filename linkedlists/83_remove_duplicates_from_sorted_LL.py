"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ex. 1
    head = [1,1,2]
    out =  [1,2]

ex. 2
    head = [1,1,2,3,3]
    out = [1,2,3]

"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def solution1(head: ListNode): 
    curr = head
    while curr and curr.next: 
        if curr.val == curr.next.val: 
            curr.next = curr.next.next
        else: 
            curr = curr.next
    return head

def solution2(head: ListNode): 

    prev = head 
    current = head.next

    while current: 
        # If the current node's value is equal to the previous node - delete the current node
        if current.val == prev.val: 
            prev.next = current.next
            current = current.next
        # Move the pointers forward
        else: 
            prev = current
            current = current.next
    return head


t = ListNode(1, ListNode(2, ListNode(3, ListNode(3)))) 
# print(solution(t))
s = solution3(t)


