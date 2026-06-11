class Solution:
    def assignEdgeWeights(self, edges):
        import collections
        MOD = 10**9 + 7

        # Step 1: Build adjacency list
        n = len(edges) + 1
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: BFS to find max depth
        visited = [False] * (n + 1)
        queue = collections.deque([(1, 0)])  # (node, depth)
        visited[1] = True
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append((nei, depth + 1))

        # Step 3: Compute number of ways
        return pow(2, max_depth - 1, MOD)
