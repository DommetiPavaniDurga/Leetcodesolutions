from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Step 1: Rotate the box 90° clockwise
        rotated = [[""] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]
        
        # Step 2: Apply gravity column by column
        for col in range(m):
            empty_row = n - 1  # start from bottom
            for row in range(n - 1, -1, -1):
                if rotated[row][col] == '*':
                    # obstacle resets empty slot tracking
                    empty_row = row - 1
                elif rotated[row][col] == '#':
                    # move stone down if possible
                    if row != empty_row:
                        rotated[empty_row][col] = '#'
                        rotated[row][col] = '.'
                    empty_row -= 1
        
        return rotated
