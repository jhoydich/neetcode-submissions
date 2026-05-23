# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        return self.BFS([root])
    def BFS(self, nodes: Optional[[TreeNode]]) -> List[List[int]]:
        if len(nodes) == 0:
            return []
        nxt_nodes = []
        vals = []
        for node in nodes:
            vals.append(node.val)
            if node.left is not None:
                nxt_nodes.append(node.left)
            if node.right is not None:
                nxt_nodes.append(node.right)
        
        prev_vals = self.BFS(nxt_nodes)
        prev_vals.insert(0, vals)
        return prev_vals
        
