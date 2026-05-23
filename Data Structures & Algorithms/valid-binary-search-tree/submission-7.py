# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.CheckNode(root, None, None)
    
    def CheckNode(self, node: Optional[TreeNode], lowerLim: Optional[int], upperLim: Optional[int]) -> bool:
        if node == None:
            return True
        
        if upperLim != None and node.val >= upperLim:
            return False
        elif lowerLim != None and node.val <= lowerLim:
            return False
        
        # check left, the upper limit will be the current nodes value
        leftCheck = self.CheckNode(node.left, lowerLim, node.val)
        
        # check right, the lower limit will be the current nodes value
        rightCheck = self.CheckNode(node.right, node.val, upperLim)

        if leftCheck == False or rightCheck == False:
            return False

        return True