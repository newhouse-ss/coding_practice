# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # given the root and subRoot, just design a function to check whether subRoot denotes a subtree of the tree with root.
        def is_same(root1, root2):
            # check whether 2 trees are same.
            if not root1 and not root2:
                return True
            if not root1 and root2 or not root2 and root1:
                return False
            if root1.val != root2.val:
                return False
            
            # root1.val == root2.val
            left = is_same(root1.left, root2.left)
            right = is_same(root1.right, root2.right)

            return left and right
        
        def dfs(root, subRoot):
            # this method travase the root-tree, on each node, check whether they are same with subRoot-tree.
            if not root:
                return False

            if is_same(root, subRoot):
                return True
            
            left_same = dfs(root.left, subRoot)
            right_same = dfs(root.right, subRoot)

            if left_same or right_same:
                return True
            else:
                return False
        
        return dfs(root, subRoot)