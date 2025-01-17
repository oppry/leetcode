# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def houxu(p):
    if p == None:
        return []
    return houxu(p.left) + houxu(p.right) + [p.val]

def houxu_dd(p):
    if p == None:
        return []
    n_stack = [[None, 0]]
    cur, sign = p, 0
    ret = []
    while cur:
        if sign:
            ret += [cur.val]
        else:
            n_stack.append([cur, 1])
            if cur.right:
                n_stack.append([cur.right, 0])
            if cur.left:
                n_stack.append([cur.left, 0])
        cur, sign = n_stack.pop()
    return ret

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return houxu_dd(root)
        