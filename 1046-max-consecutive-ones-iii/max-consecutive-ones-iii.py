class Solution(object):
    def longestOnes(self, nums, k):
        ml=0
        left=0
        z=0
        for r in range(len(nums)):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[left]==0:
                    z-=1
                left+=1
            ml=max(ml,r-left+1)
        return ml
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        