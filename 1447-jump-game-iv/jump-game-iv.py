class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph=defaultdict(list)
        for i,val in enumerate(arr):
            graph[val].append(i)
        q=deque([0])
        visited={0}
        steps=0
        while q:
            for _ in range(len(q)):
                i=q.popleft()
                if i==len(arr)-1:
                    return steps
                for j in graph.pop(arr[i],[]):
                    if j not in visited:
                        visited.add(j)
                        q.append(j)
                for j in [i-1,i+1]:
                    if 0<=j<len(arr) and j not in visited:
                        visited.add(j)
                        q.append(j)
            steps+=1
    
    