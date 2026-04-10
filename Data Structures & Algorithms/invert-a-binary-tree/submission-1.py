# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # we want the dfs return the root of the inverted tree.
            if not node:
                return
            
            left = dfs(node.left) # root of the reversed left tree
            right = dfs(node.right) # root of the reversed right tree

            temp = TreeNode()
            temp.left = left
            temp.right = right

            node.left = temp.right
            node.right = temp.left

            return node
            
        return dfs(root)