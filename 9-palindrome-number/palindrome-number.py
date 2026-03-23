class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert to string and check if it equals its reverse
        return str(x) == str(x)[::-1]
        