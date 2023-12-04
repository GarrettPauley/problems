""" 
Given a linked list, check if it is a palindrome (same forwards and backwards)

"""
from LinkedList import ListNode

def reverse(head: ListNode) -> ListNode: 

    if head.next == None: # Only one node
        return head 

    current = head
    prev = None
    nextNode = None

    while current: 
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev


        

def solution(head: ListNode) -> False:
    first_half = [] 
    second_half_reversed = []
    fast = head 
    slow = head
    while fast and fast.next: 
        first_half.append(slow.val)
        fast = fast.next.next
        slow = slow.next
    # slow is at the midpoint
    reversed_from_mid = reverse(slow)
    while reversed_from_mid: 
        second_half_reversed.append(reversed_from_mid.val)
        reversed_from_mid = reversed_from_mid.next

    for i in range(len(first_half)): 
        if first_half[i] != second_half_reversed[i]: 
            return False
    return True

t = ListNode(1,ListNode(2, ListNode(2, ListNode(1))))
t2 = ListNode(1,ListNode(2, ListNode(2, ListNode(2))))
t3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(solution(t))
print(solution(t2))
print(solution(t3))


