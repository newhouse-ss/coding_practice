# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # the 1st element in the pre-order sequence should be root, so the part in the inorder sequence before root is the left subtree. If we know the left-subtree and right-subtree, I can find the root of them in the pre-order sequence acordingly.
        # 函数做的事情就是返回构建好的树的根结点。
        # 找到根节点-->正确划分pre-order和in-order中代表左右子树的部分，递归进左右子树得到左子树的根和右子树的根
        # 哎我操沟槽的 inorder.index(preorder[0])找下标，另外写递归的时候一定要时刻关注递归函数本身的定义以及怎么构建子问题的递归。
        if not preorder:
            return None
        
        value = preorder[0]
        idx = inorder.index(value) # the root's index in inorder.

        left = self.buildTree(preorder = preorder[1 : 1+idx], inorder = inorder[:idx])
        right = self.buildTree(preorder = preorder[1+idx:], inorder = inorder[idx+1:])

        root = TreeNode(value)
        root.left = left
        root.right = right

        return root