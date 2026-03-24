class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # Pointer for the position of the next unique element
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1