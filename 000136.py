def abc(nums):    
    s = list(nums)
    s.sort()
    re = 0
    for i in s:
        re = re + i
        re = -re
    return -re

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        p = 0
        for i in nums:
            p = p ^ i
        #print(p)
        return p
    