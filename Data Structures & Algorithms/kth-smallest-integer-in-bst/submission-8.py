# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        self.DFS(root)

        return self.result


    def DFS(self, node: Optional[TreeNode]):
        if node == None or self.result != None:
            return
        
        self.DFS(node.left)

        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        
        self.DFS(node.right)

        


        


        