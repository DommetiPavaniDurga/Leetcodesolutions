class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        left=0
        ml=0
        chset=set()
        for r in range(n):
            while s[r] in chset:
                chset.remove(s[left])
                left+=1
            chset.add(s[r])
            ml=max(ml,r-left+1)
        return ml

        """
        :type s: str
        :rtype: int
        """
        