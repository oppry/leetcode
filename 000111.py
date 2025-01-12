# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def qianxu(p, level):
    if(p == None):
        return 0
    if p.left == None and p.right == None:
        return level
    ret1 = ret2 = 0
    if(p.left):
        ret1 = qianxu(p.left, level + 1) 
    if(p.right):
        ret2 = qianxu(p.right, level + 1)
    if( ret1 * ret2 == 0):
        return max(ret1, ret2)
    else:
        return min(ret1, ret2)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return qianxu(root, 1)
    