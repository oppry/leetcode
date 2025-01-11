class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while(low < high - 2):
            mid = int((high + low) / 2)
            #print("1-> ", low, mid, high, end="")
            if(target == nums[mid]):
                return mid
            if(target < nums[mid]):
                high = mid
            else:
                low = mid
            #print(" -> ", low, mid, high, target, nums[mid])
        #print("2-> ", low, mid, high, target, nums[mid])
        for i in range(low, high + 1):
            #print("3-> ", i, target, nums[i])
            if(target <= nums[i]):
                return i
        else:
            return i + 1
