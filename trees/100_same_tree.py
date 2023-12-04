import unittest
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
 """

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q): 
    oneTree = preOrder(p, [])
    twoTree = preOrder(q, [])
    print(oneTree) 
    print(twoTree)
    if(len(oneTree) != len(twoTree)): 
        return False
    for i in range(len(oneTree) - 1): 
        if oneTree[i] != twoTree[i]: 
            return False
    return True

def preOrder( n: TreeNode, tracker: List): 
    if n == None: 
        tracker.append(None)
    if(n != None): 
        tracker.append(n.val)
        preOrder(n.left, tracker)
        preOrder(n.right, tracker)
    return tracker



# Tree 1
Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)

Node1.left = Node2
Node1.right = Node3
# Tree 2
Node4 = TreeNode(1)
Node5 = TreeNode(2)
Node6 = TreeNode(3)

Node4.left = Node5
Node4.right = Node6
print(isSameTree(Node4, Node1)) # Should be True


# Tree 1
NullNode = TreeNode(None)

T1 = TreeNode(1, TreeNode(2), None)
T2 = TreeNode(1, None, TreeNode(2))

print(isSameTree(T1,T2)) # Should be False
