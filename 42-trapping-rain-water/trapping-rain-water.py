class Solution(object):
    def trap(self, height):
        n=len(height)
        lm=rm=water=0
        l=0
        r=n-1
        while l<r:
            if height[l]<height[r]:
                water+=max(0,lm-height[l])
                lm=max(lm,height[l])
                l+=1
            else:
                water+=max(0,rm-height[r])
                rm=max(rm,height[r])
                r-=1
        return water

        