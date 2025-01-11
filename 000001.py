class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        s = {}
        for i in range(n):
            v = nums[i]
            t = s.get(v, None)
            if (t != None):
                return [i,t]
            s[target - v] = i
