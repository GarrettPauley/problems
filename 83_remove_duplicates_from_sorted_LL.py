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


def solution(head: ListNode): 
    vals = []
    unique_nodes = []
    while head != None: 
        if head.val not in vals: 
            vals.append(head.val)
            unique_nodes.append(head)
        head = head.next
    print ([x.val for x in unique_nodes])
    unique_nodes.sort(key= lambda x: x.val, reverse=True)
    newHead = unique_nodes.pop()
    while unique_nodes: 
        newHead.next = unique_nodes.pop()
        newHead = newHead.next
    return head

def solution2(head: ListNode): 
    unique_vals = []
    new = ListNode(head.val)
    unique_vals.append(head.val)
   
    while head:
        if head.val not in unique_vals: 
            unique_vals.append(head.val)
            new.next = head
            new = new.next
        head = head.next
        continue
    return new


def printTest(node: ListNode): 
    while node: 
        print(node.val)
        node = node.next

def solution3(head: ListNode): 
    curr = head
    while curr and curr.next: 
        if curr.val == curr.next.val: 
            curr.next = curr.next.next
        else: 
            curr = curr.next
    return head


t = ListNode(1, ListNode(2, ListNode(3, ListNode(3)))) 
# print(solution(t))
s = solution3(t)
printTest(s)



