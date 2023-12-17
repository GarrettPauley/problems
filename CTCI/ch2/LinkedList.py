
class ListNode: 
    def __init__(self, val, next = None): 
        self.val = val 
        self.next = next

    def addNodeToEnd(self, head, node_to_add): 
        if head == None: 
            return node_to_add
        n = head
        while n.next:
            n = n.next
        n.next = node_to_add
        return head
    
    def addNodeAtBeginning(self, head, data): 
        newNode = ListNode(data)
        if head == None: 
            return newNode
        newNode.next = head
        return newNode
    
    def hasLoop(self, head): 
        slow = head
        fast = head

        while fast and fast.next: # even nodes: fast.next will be null. Odd nodes: fast will be null.
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        return False



    def deleteNode(self,head, val_to_delete: int): 
        if head == None: 
            return head
        n = head
        if n.val == val_to_delete: 
            return n.next
        while n.next: 
            if n.next.val == val_to_delete: 
                n.next = n.next.next
            n = n.next
        return head
    
    def valueInList(self, head, val_to_find): 
        temp = head
        while(temp != None): 
            if(temp.val == val_to_find): 
                return True
            temp = temp.next
        return False




    def __str__(self) -> str:
        node_vals = []
        n = self
        if self.hasLoop(n): 
            return "has loop"
            # while n not in node_vals: 
                # node_vals.append(str(n.val))
                # n = n.next
            # return ' -> '.join(node_vals)
        while n: 
            node_vals.append(str(n.val))
            n = n.next
        return ' -> '.join(node_vals)

def printLL(head) -> str:
    node_vals = []
    n = head
    while n.next: 
        node_vals.append(str(n.val))
        n = n.next
    print(' -> '.join(node_vals))



# Some operation
# n.deleteNode(n, 2)
# n.addNodeToEnd(n, ListNode(4))
# n.addNodeAtBeginning(n, ListNode(8))
# printLL(n2)
# print(n.valueInList(n, 3)) #should be true
# print(n.valueInList(n, 8)) #should be False



