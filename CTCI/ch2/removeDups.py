""" 
write a function that takes a reference to the head of a linked listand removes the duplicates

"""
from LinkedList import ListNode

def solution(head: ListNode) -> ListNode: 
    if not head: # No elements
        return None
    if head.next == None: # only one element
        return head 
    vals = [] 
    temp = head
    vals.append(temp.val)
    while temp.next: 
        if temp.next.val not in vals: # unique value
            vals.append(temp.next.val)
            temp = temp.next
        else: # duplicate value reached
            temp.next = temp.next.next # delete it. 
    return head


t = ListNode(1, ListNode(1, ListNode(2)))
t2 = ListNode(None)
t3 = ListNode(1, ListNode(2, ListNode(2, ListNode(1, ListNode(2)))))
print(solution(t))
print(solution(t2))
print(solution(t3))
        
        