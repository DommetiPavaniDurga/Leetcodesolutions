class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        dp=[False]*n
        dp[0]=True
        prefix=[0]*(n+1)
        prefix[1]=1
        for i in range(1,n):
            if s[i]=='0':
                left=max(0,i-maxJump)
                right=i-minJump
                if right>=0 and prefix[right+1]-prefix[left]>0:
                    dp[i]=True
            prefix[i+1]=prefix[i]+(1 if dp[i] else 0)
        return dp[-1]