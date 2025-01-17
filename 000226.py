# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def changeT(p):
    if p == None:
        return p
    if p.left:
        changeT(p.left)
    if p.right:
        changeT(p.right)
    p.left, p.right = p.right, p.left
    return p

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return changeT(root)
        