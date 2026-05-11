class Solution:
    def separateDigits(self, nums):
        ans = []
        for num in nums:
            for c in str(num):
                ans.append(int(c))
        return ans
