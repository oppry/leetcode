class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = dict()
        for i in range(len(nums)):
            if nums[i] in s and (i - s[nums[i]]) <= k:
                    return True
            else:
                s[nums[i]] = i
        return False
    