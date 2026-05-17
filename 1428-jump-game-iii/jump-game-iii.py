class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=deque([start])
        while q:
            i=q.popleft()
            if arr[i]==0:
                return True
            if arr[i]<0:
                continue
            jump=arr[i]
            arr[i]=-1
            if i + jump < len(arr):
                q.append(i + jump)
            if i - jump >=0:
                q.append(i-jump)
        return False