# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # There're only 3 cases: p, q in left and right subtree of LCA separately; both p, q in the left subtree of LCA; or right.
        if not root or root.val == p.val or root.val == q.val:
            return root # means we find p/q or not.
        
        left = self.lowestCommonAncestor(root.left, p, q) # not None when left subtree contains at least one p/q
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # one of p/q is in left subtree and the other is in right. So the current root is LCA (if lower, p and q will be separaed)
            return root
        
        return left if left else right