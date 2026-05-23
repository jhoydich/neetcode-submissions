# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.DFS(root))
    
    def DFS(self, node) -> List[int]:
        if node == None:
            return [None, None]
        
        left_val, maxLowerPathL = self.DFS(node.left)
        right_val, maxLowerPathR  = self.DFS(node.right)

        
        max_half = max([(0 if left_val is None else left_val) + node.val, (0 if right_val is None else right_val) + node.val, node.val])
        max_path = max([(maxLowerPathL or -1001), (maxLowerPathR or -1001), (right_val or 0) + (left_val or 0) + node.val , (left_val or -1001), (right_val or -1001)])
        print(max_half, max_path)
        return [max_half, max_path]

        

        