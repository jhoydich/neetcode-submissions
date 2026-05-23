# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.explore(root, 0)
        

    def explore(self, node: Optional[TreeNode], depth: int) ->int:
        if node == None:
            return depth
        depth_l = self.explore(node.left, depth+1)
        depth_r = self.explore(node.right, depth+1) 
        return max([depth_l, depth_r])   

    
        