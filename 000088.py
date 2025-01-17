class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m = m - 1
        n = n - 1
        for i in range(m + n + 1, -1, -1):
            #print(i,m,n)
            if(n < 0):
                break
            if(m >= 0 and nums1[m] >= nums2[n]):
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            #print(i, nums1)
        