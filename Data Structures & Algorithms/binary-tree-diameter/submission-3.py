# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam, max_length = self.explore(root)
        return diam

    def explore(self, node: Optional[TreeNode]) -> [int, int]:
        if node == None:
            return [0, 0]
        if node.left == None and node.right == None:
            return [0, 1]
        max_path_l, max_length_l = self.explore(node.left)
        max_path_r, max_length_r = self.explore(node.right)
        max_cross_path = max_length_r + max_length_l

        return [max([max_path_l, max_path_r, max_cross_path]), max([max_length_r+1, max_length_l+1])]


