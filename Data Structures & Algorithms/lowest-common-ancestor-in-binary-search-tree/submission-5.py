# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        m_node, m = self.DFS(root, p, q)
        return m_node
    def DFS(self, node: Optional[TreeNode], p: TreeNode, q: TreeNode):
        if node == None:
            return [None, None]
        
        llca_node, l_node = self.DFS(node.left, p, q)
        rlca_node, r_node = self.DFS(node.right, p, q)

        if llca_node != None:
            return [llca_node, None]
        if rlca_node != None:
            return [rlca_node, None]

        if (node.val == p.val and l_node is not None) or (node.val == q.val and l_node is not None):
            return [node, None]
        
        if (node.val == p.val and r_node is not None) or (node.val == q.val and r_node is not None):
            return [node, None]

        if node.val == p.val or node.val == q.val:
            return [None, node]
        
        if l_node is not None and r_node is not None:
            return [node, None]
        elif l_node is not None:
            return [None, l_node]
        elif r_node is not None:
            return [None, r_node]
        
        return [None, None]
        
