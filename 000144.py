# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def qianxu(p):
    if p == None:
        return []
    return [p.val] + qianxu(p.left) + qianxu(p.right)

def qianxu_dd(p):
    if p == None:
        return []
    n_stack= [None]
    cur = p
    ret = []
    while(cur):
        ret = ret + [cur.val]
        if(cur.right):
            n_stack.append(cur.right)
        if(cur.left):
            n_stack.append(cur.left)
        cur = n_stack.pop()
    return ret
    

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return qianxu_dd(root)
    