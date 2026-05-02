class Solution:
    def rotatedDigits(self, n: int) -> int:
        mapping = {0:0, 1:1, 2:5, 5:2, 6:9, 9:6, 8:8}
        count = 0
        
        for num in range(1, n+1):
            temp, rotated, valid = num, 0, True
            place = 1
            
            while temp > 0:
                digit = temp % 10
                if digit not in mapping:  # invalid digit (3,4,7)
                    valid = False
                    break
                rotated += mapping[digit] * place
                place *= 10
                temp //= 10
            
            if valid and rotated != num:  # must change to be "good"
                count += 1
        
        return count
