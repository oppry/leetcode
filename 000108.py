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

def qianxu_left_vs_right(p):
    if(p == None):
        return [0, 0]
    ll = qianxu_sd(p.left)
    rl = qianxu_sd(p.right)
    return [max(ll, rl) + 1, rl - ll]

def addBST(root, p):
    if(root == None):
        root = TreeNode(p)
    else:
        if(p <= root.val):
            if(root.left):
                addBST(root.left, p)
            else:
                root.left = TreeNode(p)
        else:
            if(root.right):
                addBST(root.right, p)
            else:
                root.right = TreeNode(p)
    return root

def rotatoBST(p, level):
    # rotato to right
    new_root = p
    if(level < -1):
        if(p.left):
            new_root = p.left
            p.left = p.left.right
            new_root.right = p
    if(level > 1):
        if(p.right):
            new_root = p.right
            p.right = p.right.left
            new_root.left = p
    return new_root

def new_list(p):
    if(len(p) <= 1):
        return p
    midle = int(len(p) / 2)
    return [p[midle]] + new_list(p[:midle]) + new_list(p[midle + 1:])

def abc(nums):
    # nums = [0,1,2,3,4,5]
    new_nums = new_list(nums)
    root = None
    for i in new_nums:
        root = addBST(root, i)
    return root

def abcd(nums):
    if(len(nums) == 0):
        return None
    count = len(nums) // 2
    return TreeNode(nums[count], abcd(nums[:count]), abcd(nums[count + 1:]))

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if(len(nums) == 0):
            return None
        count = len(nums) // 2
        return TreeNode(nums[count], self.sortedArrayToBST(nums[:count]), self.sortedArrayToBST(nums[count + 1:]))
        