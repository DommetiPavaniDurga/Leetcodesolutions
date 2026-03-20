class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ends=[]
        for s,e in intervals:
            ends.append((e,s))
        ends.sort()
        c=0
        le=ends[0][0]
        for e,s in ends[1:]:
            if s<le:
                c+=1
            else:
                le=e
        return c