class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        cnt=0
        freq={'a':0,'b':0,'c':0}
        for r in range(len(s)):
            freq[s[r]]+=1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                cnt+=len(s)-r
                freq[s[left]]-=1
                left+=1
        return cnt