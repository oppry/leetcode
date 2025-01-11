class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur = 0
        for ele in nums:
            if(ele != val):
                nums[cur] = ele
                cur += 1
        return cur
