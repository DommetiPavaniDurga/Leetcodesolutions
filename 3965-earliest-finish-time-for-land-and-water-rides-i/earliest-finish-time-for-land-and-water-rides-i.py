class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')
        for i in range(len(landStartTime)):
            land_finish=landStartTime[i]+landDuration[i]
            for j in range(len(waterStartTime)):
                water_start=max(land_finish,waterStartTime[j])
                water_finish=water_start+waterDuration[j]
                ans=min(ans,water_finish)
        for j in range(len(waterStartTime)):
            water_finish=waterStartTime[j]+waterDuration[j]
            for i in range(len(landStartTime)):
                land_start=max(water_finish,landStartTime[i])
                land_finish=land_start+landDuration[i]
                ans=min(ans,land_finish)
        return ans   