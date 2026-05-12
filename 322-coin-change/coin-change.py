class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        if amount == 0:
            return 0

        queue = deque()
        queue.append((0,0))

        visitedAmount=set()
        visitedAmount.add(0)

        while queue:
            currentSum,no_of_coins=queue.popleft()

            for coin in coins:
                nextSum=currentSum + coin

                if nextSum == amount:
                    return no_of_coins + 1

                if nextSum < amount and nextSum not in visitedAmount:
                    visitedAmount.add(nextSum)
                    queue.append((nextSum,no_of_coins + 1))

        return -1