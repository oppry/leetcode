class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        #v = nums[0]
        for i in nums:
            if i != nums[cur]:
                cur += 1
                nums[cur] = i
                
        #print(cur)
        #nums = nums[:cur]
        return cur + 1
