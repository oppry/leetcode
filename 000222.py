# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def qianxu(p):
    if p == None:
        return 0
    ret = 0
    return 1 + qianxu(p.left) + qianxu(p.right)

def treeH(p):
    count = 0
    while p:
        p = p.left
        count += 1
    return count

def solution(p):
    if p == None:
        return 0
    lh, rh = treeH(p.left), treeH(p.right)
    if lh == rh:
        return 2 ** lh + solution(p.right) 
    else:
        return 2 ** rh + solution(p.left) 

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return solution(root)

