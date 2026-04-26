class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # strip trailing spaces, then split
        words = s.strip().split()
        return len(words[-1])
