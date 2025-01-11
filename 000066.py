class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        jinwei = 1
        for i in range(len(digits) -1 , -1, -1):
            if(digits[i] + jinwei < 10):
                digits[i] += 1
                break
            else:
                digits[i] = 0
                jinwei = 1
        else:
            if jinwei == 1:
               digits.insert(0, 1)
        return digits
