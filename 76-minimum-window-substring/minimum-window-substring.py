class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        freq={}
        for ch in t:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        left=0
        ml=float('inf')
        c=0
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]]>0:
                    c+=1
                freq[s[r]]-=1
            else:
                freq[s[r]]=-1
            while c==len(t):
                if r-left+1<ml:
                    ml=r-left+1
                    st=left
                freq[s[left]]+=1
                if freq[s[left]]>0:
                    c-=1
                left+=1
        if ml==float('inf'):
            return ""
        else:
            return s[st:st+ml]

