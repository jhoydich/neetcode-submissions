# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS and choose the rightmost node on every level
        if root == None:
            return []
        levels = self.BFS([root])
        out = []
        for level in levels:
            out.append(level[-1])
        return out
    
    def BFS(self, nodes: List[TreeNode]) -> List[List[int]]:
        if len(nodes) == 0:
            return []
        
        vals = []
        nxt_nodes = []

        for node in nodes:
            vals.append(node.val)
            if node.left != None:
                nxt_nodes.append(node.left)
            if node.right != None:
                nxt_nodes.append(node.right)
        
        prev_vals = self.BFS(nxt_nodes)
        prev_vals.insert(0, vals)
        return prev_vals