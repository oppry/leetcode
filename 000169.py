def check(nums):
    d = dict()
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 0
    max_c = 0
    max_ele = None
    for i in d:
        if d[i] >= max_c:
            max_c = d[i]
            max_ele = i
    return max_ele    

def check0(nums):
    nums.sort()
    return nums[len(nums) // 2]

def check8(nums):
    can, c = 0, 0
    for i in nums:
        if c == 0:
            can, c = i, 1
        else:
            if(i == can):
                c += 1
            else:
                c -= 1
    return can

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #nums = [6,5,5]
        can, c = 0, 0
        for i in nums:
            if c == 0:
                can, c = i, 1
            else:
                c = c + (1 if i == can else -1)
        return can

