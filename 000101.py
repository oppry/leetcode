# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def qianxu(root):
    if(root == None):
        return []
    ret = [root.val]
    if root.left:
        ret += qianxu(root.left) 
    if root.right:
        ret += qianxu(root.right)
    return ret

def qianxu_dd(root):
    n_stack = [[None, 0]]
    cur, sign = [root, 0]
    ret = []
    while(cur):
        ret.append(cur.val)
        if(cur.right):
            n_stack.append([cur.right, 0])
        if(cur.left):
            n_stack.append([cur.left, 0])
        cur,sign = n_stack.pop()
    return ret

def qianxu_dd_simple(root):
    n_stack = [None]
    cur = root
    ret = []
    while(cur):
        ret.append(cur.val)
        if(cur.right):
            n_stack.append(cur.right)
        if(cur.left):
            n_stack.append(cur.left)
        cur = n_stack.pop()
    return ret

def zhongxu(root):
    ret = []
    if(root == None):
        return []
    if root.left:
        ret += zhongxu(root.left) 
    ret += [root.val]
    if root.right:
        ret += zhongxu(root.right)
    return ret   

def zhongxu_dd(root):
    n_stack = [[None, 0]]
    cur, sign = [root, 0]
    ret = []
    while(cur):
        if sign == 1:
            ret.append(cur.val)
        else:
            if(cur.right):
                n_stack.append([cur.right, 0])
            n_stack.append([cur, 1])
            if(cur.left):
                n_stack.append([cur.left, 0])
        cur,sign = n_stack.pop()
    return ret

def houxu(root):
    ret = []
    if(root == None):
        return []
    if root.left:
        ret += houxu(root.left) 
    if root.right:
        ret += houxu(root.right)
    ret += [root.val]
    return ret   

def houxu_dd(root):
    n_stack = [[None, 0]]
    cur, sign = [root, 0]
    ret = []
    while(cur):
        if sign == 1:
            ret.append(cur.val)
        else:
            n_stack.append([cur, 1])
            if(cur.right):
                n_stack.append([cur.right, 0])
            if(cur.left):
                n_stack.append([cur.left, 0])
        cur,sign = n_stack.pop()
    return ret

def compare_2_tree(p, q):
    #cur_p, cur_q = p, q
    if( p == None and q == None):
        return True
    if(p == None or q == None):
        return False
    if(p.val != q.val):
        return False
    return compare_2_tree(p.left, q.left) and compare_2_tree(p.right, q.right)

def compare_2_tree_duicheng(p, q):
    #cur_p, cur_q = p, q
    if( p == None and q == None):
        return True
    if(p == None or q == None):
        return False
    if(p.val != q.val):
        return False
    return compare_2_tree_duicheng(p.left, q.right) and compare_2_tree_duicheng(p.right, q.left)

def compare_2_tree_duicheng_dd(p, q):
    n_stack = [[None, None]]
    p_cur = p
    q_cur = q
    while(p_cur != None or q_cur != None):
        if(p_cur == None or q_cur == None):
            return False
        if(p_cur.val != q_cur.val):
            return False
        if(p_cur.left or q_cur.right):
            n_stack.append([p_cur.left, q_cur.right])
        if(p_cur.right or q_cur.left):
            n_stack.append([p_cur.right, q_cur.left])
        p_cur, q_cur = n_stack.pop()
    return True

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #print(qianxu(root))
        #print(qianxu_dd(root))
        #print(qianxu_dd_simple(root))
        #print(zhongxu(root))
        #print(zhongxu_dd(root))
        #print(houxu(root))
        #print(houxu_dd(root))
        return compare_2_tree_duicheng_dd(root.left, root.right)
