# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def qianxu_sd(p):
    if(p == None):
        return 0
    return max(qianxu_sd(p.left), qianxu_sd(p.right)) + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return qianxu_sd(root)
    