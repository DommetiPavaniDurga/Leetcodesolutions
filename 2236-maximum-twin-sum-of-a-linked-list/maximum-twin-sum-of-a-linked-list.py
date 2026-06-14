class Solution:
    def pairSum(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        ans = 0
        n = len(arr)

        for i in range(n // 2):
            ans = max(ans, arr[i] + arr[n - 1 - i])

        return ans