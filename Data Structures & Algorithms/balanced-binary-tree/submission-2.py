# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h, bal = self.explore(root)
        return bal

    # explore checks the left and right tree heights, returns the 
    # max side height and whether the sub-tree is balanced
    def explore(self, node: Optional[TreeNode]) -> [int, bool]:
        if node == None:
            return [0, True]
        left_h, left_bal = self.explore(node.left)
        right_h, right_bal = self.explore(node.right)

        if left_bal == False or right_bal == False:
            return [0, False]
        if abs(left_h - right_h) > 1:
            return [0, False]
        
        return [max(left_h+1, right_h+1), True]
        