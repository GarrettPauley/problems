""" 
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

e.g., ( 7 -> 1 -> 6  ) + (5 -> 9 -> 2)  = 617 + 295 = (2 -> 1 -> 9) = 912 

"""

from LinkedList import ListNode

def solution(head1, head2): 
    vals1 = []
    vals2 = []

    while head1: 
        vals1.append(str(head1.val))
        head1 = head1.next
    while head2: 
        vals2.append(str(head2.val))
        head2 = head2.next

    a = int(''.join(reversed(vals1)))
    b = int(''.join((reversed(vals2))))
    s = str(a + b)
    s = s[::-1]

    
    newList = ListNode(int(s[0]))
    temp = newList
    for i in range(1, len(s)): 
        temp.next = ListNode(int(s[i]))
        temp = temp.next
    return newList

    

t = ListNode(0, ListNode(0, ListNode(3)))
t2 = ListNode(0, ListNode(0, ListNode(2)))
print(solution(t, t2))


