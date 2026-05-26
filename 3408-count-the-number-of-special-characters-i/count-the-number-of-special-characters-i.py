class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        count=0

        for a,b in zip(string.ascii_lowercase,string.ascii_uppercase):
            if a in s and b in s:
                count+=1
        return count