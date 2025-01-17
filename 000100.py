# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bianli_tree1(p):
    node_st = [None]
    ret = []
    cur = [p, 0, 0]
    level = 0
    while(cur and cur[0]):
        #print("1 -", cur[0].val, cur[1], node_st)
        level = cur[2]
        if(cur[1] == 0):
            if cur[0].left:
                node_st.append([cur[0], -1, level])
                cur = [cur[0].left, 0, level+1]
                continue
            else:
                ret.append(f"left{level+1}")
        if(cur[1] != 1):
            ret.append(cur[0].val)
            if(cur[0].right):
                node_st.append([cur[0], 1, level])
                cur = [cur[0].right, 0, level + 1]
                continue
            else:
                ret.append(f"right{level+1}")
        cur = node_st.pop()
    return ret

def com_p_q(p,q):
    ret_p = bianli_tree1(p)
    ret_q = bianli_tree1(q)
    if( ret_p == ret_q):
        return True
    else:
        return False

def compare_2_tree(p, q):
    #cur_p, cur_q = p, q
    if( p == None and q == None):
        return True
    if(p == None or q == None):
        return False
    if(p.val != q.val):
        return False
    return compare_2_tree(p.left, q.left) and compare_2_tree(p.right, q.right)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return compare_2_tree(p, q)
