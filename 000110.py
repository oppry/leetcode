# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def level_BST(p):
    if(p == None):
        return 0
    l_level = level_BST(p.left)
    r_level = level_BST(p.right)
    return max(l_level, r_level) + 1

def qianxu_dd(p):
    bianli = []
    n_stack = [None]
    cur = p
    while(cur):
        bianli.append(cur.val)
        if(cur.right):
            n_stack.append(cur.right)
        if(cur.left):
            n_stack.append(cur.left)
        #print(bianli)
        cur = n_stack.pop()
    return bianli

def check_BST(p):
    if p == None:
        return [0, True]
    pl, l_re = check_BST(p.left)
    pr, r_re = check_BST(p.right)
    if(l_re == False or r_re == False):
        return [max(pl, pr) + 1, False]
    if(max(pl, pr) - min(pl, pr) <= 1):
        return [max(pl, pr) + 1, True]
    else:
        return [max(pl, pr) + 1, False]

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #print(qianxu_dd(root))        
        return check_BST(root)[1]
    