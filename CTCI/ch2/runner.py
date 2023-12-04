""" 
suppose you had a linked list a1 -> a2 -> a3 -> ... a-n -> b1 -> b2 -> b3 -> b-n

We don't know how many elements are in the list, but we know that there are an even number of elements
we want to return a1 -> b1 -> a2 -> b2 ... -> a-n -> b-n

We will use the 'runner' method. We have a fast and slow pointer. The fast pointer is twice as fast as the slow 
pointer. When the fast pointer reaches the end of the list, the slow pointer will be in the middle. 

When we get to that point, we will move the fast pointer back to the beginning. 
point a1 to slow (b1), point slow to a1.next. 

"""
from LinkedList import ListNode
def weave(head: ListNode):
    if not head:
        return None

    slow = head
    fast = head
    # runner - move the fast pointer twice as fast until we get to the end.
    while fast: 
        slow = slow.next
        fast = fast.next.next
    fast = head # move the fast pointer back to the beginning. 
    while slow:
        temp1 = fast.next
        temp2 = slow.next 

        slow.next = fast.next
        fast.next = slow

        fast = temp1
        slow = temp2
    return head

        


t = ListNode('a1', ListNode('a2', ListNode('b1', ListNode('b2', None))))
print(t)
a = weave(t)


#print(weave(t)




