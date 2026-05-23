# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.DFS(root, -101)


    def DFS(self, node: Optional[TreeNode], maxVal: int) -> int:
        if node == None:
            return 0
        
        good = 0
        if node.val >= maxVal:
            maxVal = node.val
            good = 1
        
        left_val = self.DFS(node.left, maxVal)
        right_val = self.DFS(node.right, maxVal)
        return good + left_val + right_val