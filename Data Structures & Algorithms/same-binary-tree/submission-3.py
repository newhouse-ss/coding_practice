# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            # the function of this method is to compare whether the given 2 trees are same.
            if not node1 and not node2:
                return True

            if not node1 and node2 or not node2 and node1:
                return False
            
            # now, both of node1 and node 2 are existing
            if node1.val != node2.val:
                return False
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right
        
        return dfs(p, q)