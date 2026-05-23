# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Node existence check
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        
        # Node value check
        if p.val != q.val:
            return False

        # recursively check the subtree
        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)
        if left_check == False or right_check == False:
            return False
        
        # we passed all of our checks
        return True
    