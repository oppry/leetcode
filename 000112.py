# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sum_tree(p, sum, targetsum):
    if(p == None):
        return False
    sum = sum + p.val
    re1 = re2 = False
    if(p.left):
        re1 = sum_tree(p.left, sum, targetsum)
    if(p.right):
        re2 = sum_tree(p.right, sum, targetsum)
    if(p.left == None and p.right == None):
        return sum == targetsum
    else:
        return re1 or re2

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0
        return sum_tree(root, sum, targetSum)
    