from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []
        
        for i in range(word_len):  # offset to handle alignment
            left = i
            curr_count = Counter()
            count = 0
            
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    curr_count[word] += 1
                    count += 1
                    
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == len(words):
                        result.append(left)
                else:
                    curr_count.clear()
                    count = 0
                    left = j + word_len
        
        return result
