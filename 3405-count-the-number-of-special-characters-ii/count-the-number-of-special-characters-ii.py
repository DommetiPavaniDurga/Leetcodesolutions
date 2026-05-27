class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper={}
        last_lower={}
        for i,c in enumerate(word):
            if c.islower():
                last_lower[c]=i
            else:
                if c not in first_upper:
                    first_upper[c]=i
        count=0
        for a,b in zip(string.ascii_lowercase,string.ascii_uppercase):
            if a in last_lower and b in first_upper and last_lower[a]<first_upper[b]:
                count+=1
        return count