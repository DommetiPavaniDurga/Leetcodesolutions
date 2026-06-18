class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * (n + 1)  # lengths[i] = length after processing s[:i]

        # Forward pass: compute lengths
        for i in range(n):
            if s[i].isalpha():
                lengths[i+1] = lengths[i] + 1
            elif s[i] == '*':
                lengths[i+1] = max(0, lengths[i] - 1)
            elif s[i] == '#':
                lengths[i+1] = lengths[i] * 2
            elif s[i] == '%':
                lengths[i+1] = lengths[i]

        # If k is out of bounds
        if k >= lengths[n]:
            return "."

        # Backward pass: trace k back through operations
        for i in range(n-1, -1, -1):
            if s[i].isalpha():
                if k == lengths[i]:  # last appended character
                    return s[i]
            elif s[i] == '*':
                if lengths[i+1] == lengths[i] - 1 and k == lengths[i]:
                    return "."
            elif s[i] == '#':
                if k >= lengths[i]:
                    k %= lengths[i]  # map back into first half
            elif s[i] == '%':
                k = lengths[i] - 1 - k  # mirror index

        return "."
