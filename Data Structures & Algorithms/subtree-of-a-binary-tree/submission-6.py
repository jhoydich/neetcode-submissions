# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        hasSub = False
        match_nodes = self.explore(root, subRoot.val)
        for node in match_nodes:
            hasSub = self.match_tree(node, subRoot)
            if hasSub:
                break
        
        
        
        return hasSub
    def explore(self, node: Optional[TreeNode], val: Optional[int]) -> [TreeNode]:
        nodes = []
        if node == None:
            return None
        if node.val == val:
            nodes.append(node)
        l_nodes = self.explore(node.left, val)
        r_nodes = self.explore(node.right, val)

        if l_nodes != None:
            nodes.extend(l_nodes)
        if r_nodes != None:
            nodes.extend(r_nodes)
        return nodes    
    
    def match_tree(self, node: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if node == None and subRoot == None:
            return True
        
        if node.val != subRoot.val:
            return False
        if (node.left == None and subRoot.left != None) or (node.left != None and subRoot.left == None):
            return False
        if (node.right == None and subRoot.right != None) or (node.right != None and subRoot.right == None):
            return False

        left_match = self.match_tree(node.left, subRoot.left)
        right_match = self.match_tree(node.right, subRoot.right)

        if left_match == False or right_match == False:
            return False
        
        return True

